import logging

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from braces.views import SelectRelatedMixin, LoginRequiredMixin
from rest_framework import viewsets, renderers, views
from rest_framework.decorators import action, api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from accounts.models import UserProfile
from articles.forms import ArticleForm, CommentForm
from articles.models import Article, Vote, Comment

# class ArticleCreate(CreateView):
#     model = Article
#     form_class = ArticleForm
#
#     def get_redirect_url(self,*args,**kwargs):
#         return reverse('groups:topic_detail',kwargs={'slug':self.kwargs.get('slug')})
from articles.serializers import VotesSerializer, CommentsSerializer
from groups.models import Topic

User = get_user_model()


class ArticleList(SelectRelatedMixin, LoginRequiredMixin, ListView):
    model = Article
    select_related = ('userprofile', 'topic')
    #context_list = 'article_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_list = Article.objects.filter(topic=topic_name).order_by('-created_at')
        context['article_list'] = article_list
        return context


class UserArticle(ListView):
    model = Article
    template_name = 'article/user_article_list.html'

    def get_queryset(self):
        try:
            self.article_user = User.objects.prefetch_related('article').get(
                username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.article_user.articles.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_user'] = self.article_user
        return context


class ArticleDetail(SelectRelatedMixin, DetailView, CreateView):
    model = Article
    select_related = ('created_by', 'topic')
    #slug_field = 'article_name'
    slug_field = 'slug'
    template_name = 'article_detail.html'
    form_class = CommentForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.commenter = self.request.user.user_profile
        article = get_object_or_404(Article, slug=self.kwargs.get('slug'))
        self.object.article = article
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.object
        comment_list = Comment.objects.filter(article=article).order_by('-time')
        context['comment_list'] = comment_list
        vote_count = Vote.objects.filter(article=article).aggregate(Sum('value'))
        context['vote_count'] = vote_count['value__sum']
        return context

    def get_redirect_url(self,*args,**kwargs):
        return reverse('articles:article_detail',kwargs={'slug':self.slug})


class ArticleCreate(SelectRelatedMixin, LoginRequiredMixin, CreateView):
    template_name = 'article_form.html'
    model = Article
    form_class = ArticleForm
    slug_field = 'slug'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user.user_profile
        topic = get_object_or_404(Topic, slug=self.kwargs.get('slug'))
        self.object.topic = topic
        self.object.save()
        return super().form_valid(form)

    def get_redirect_url(self,*args,**kwargs):
        return reverse('articles:article_detail',kwargs={'slug': self.kwargs.get('slug')})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = get_object_or_404(Topic, slug= self.kwargs.get('slug'))
        context['topic'] = topic
        return context

class AddComment(SelectRelatedMixin, LoginRequiredMixin, CreateView):
    template_name = 'comment_form.html'
    model = Comment
    form_class = CommentForm
    slug_field = 'slug'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.commenter = self.request.user.user_profile
        article = get_object_or_404(Article, slug=self.kwargs.get('slug'))
        self.object.article = article
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articles:article_detail', kwargs={'slug': self.kwargs.get('slug')})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = get_object_or_404(Article, slug= self.kwargs.get('slug'))
        context['article'] = article
        return context


class ArticleDelete(SelectRelatedMixin, LoginRequiredMixin, DeleteView):
    model = Article
    select_related = ('created_by', 'topic')
    slug_field = 'article_name'
    template_name = 'article_delete.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Article Deleted')
        return super().delete(*args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('articles:article_list', kwargs={'slug': self.kwargs.get('slug')})

class Upvote(LoginRequiredMixin,generic.RedirectView):

    def get(self, request,*args,**kwargs):
        article = get_object_or_404(Article, slug=self.kwargs.get('slug'))
        vote = None
        try:
            vote = Vote.objects.get(voter=self.request.user.user_profile, article=article)
        except ObjectDoesNotExist:
            pass
        if vote:
            if vote.value == 1:
                logging.warning("you can't upvote twice silly")
            else:
                vote.value = 1
                vote.save()
                logging.warning("you changed your mind and upvoted")
        else:
            vote = Vote()
            vote.article = article
            vote.voter = self.request.user.user_profile
            vote.value = 1
            vote.save()
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('articles:article_detail', kwargs={'slug': self.kwargs.get('slug')})

from functools import wraps
from django.utils.decorators import available_attrs, decorator_from_middleware


def csrf_clear(view_func):
    """
    Skips the CSRF checks by setting the 'csrf_processing_done' to true.
    """

    def wrapped_view(*args, **kwargs):
        request = args[0]
        request.csrf_processing_done = True
        return view_func(*args, **kwargs)

    return wraps(view_func, assigned=available_attrs(view_func))(wrapped_view)


@csrf_clear
@api_view(['POST',])
def js_upvoting(request, pk):
    if request.method == 'POST':
        article = get_object_or_404(Article, id=pk)
        vote = None
        try:
            vote = Vote.objects.get(voter=request.user.user_profile, article=article)
        except ObjectDoesNotExist:
            pass
        if vote:
            if vote.value == 1:
                logging.warning("you can't upvote twice silly")
            else:
                vote.value = 1
                vote.save()
                logging.warning("you changed your mind and upvoted")
        else:
            vote = Vote()
            vote.article = article
            vote.voter = request.user.user_profile
            vote.value = 1
            vote.save()

    article_id = pk
    vote_count = Vote.objects.filter(article=pk).aggregate(Sum('value'))
    context = vote_count['value__sum']
    yourdata = {"article_id": article_id, "vote_count": context}
    results = VotesSerializer(yourdata).data
    return Response(results)


@csrf_clear
@api_view(['POST',])
def js_downvoting(request, pk):
    if request.method == 'POST':
        article = get_object_or_404(Article, id=pk)
        vote = None
        try:
            vote = Vote.objects.get(voter=request.user.user_profile, article=article)
        except ObjectDoesNotExist:
            pass
        if vote:
            if vote.value == -1:
                logging.warning("you can't downvote twice silly")
            else:
                vote.value = -1
                vote.save()
                logging.warning("you changed your mind and downvoted")
        else:
            vote = Vote()
            vote.article = article
            vote.voter = request.user.user_profile
            vote.value = -1
            vote.save()

    article_id = pk
    vote_count = Vote.objects.filter(article=pk).aggregate(Sum('value'))
    context = vote_count['value__sum']
    yourdata = {"article_id": article_id, "vote_count": context}
    results = VotesSerializer(yourdata).data
    return Response(results)


@csrf_clear
def js_commenting(request, pk):
    if request.method == 'GET':
        article_id = pk
        comments = Comment.objects.filter(article_id=article_id).order_by('-time')
        serializer = CommentsSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save(commenter=request.user.user_profile)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class Downvote(LoginRequiredMixin,generic.RedirectView):

    def get(self, request,*args,**kwargs):
        article = get_object_or_404(Article, slug=self.kwargs.get('slug'))
        vote = None
        try:
            vote = Vote.objects.get(voter=self.request.user.user_profile, article=article)
        except ObjectDoesNotExist:
            pass
        if vote:
            if vote.value == -1:
                logging.warning("you can't downvote twice silly")
            else:
                vote.value = -1
                vote.save()
                logging.warning("you changed your mind and downvoted")
        else:
            vote = Vote()
            vote.article = article
            vote.voter = self.request.user.user_profile
            vote.value = -1
            vote.save()
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('articles:article_detail', kwargs={'slug': self.kwargs.get('slug')})