from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from braces.views import SelectRelatedMixin, LoginRequiredMixin

from accounts.models import UserProfile
from articles.forms import ArticleForm
from articles.models import Article


# class ArticleCreate(CreateView):
#     model = Article
#     form_class = ArticleForm
#
#     def get_redirect_url(self,*args,**kwargs):
#         return reverse('groups:topic_detail',kwargs={'slug':self.kwargs.get('slug')})
from groups.models import Topic

User = get_user_model()


class ArticleList(SelectRelatedMixin, LoginRequiredMixin, ListView):
    model = Article
    select_related = ('userprofile', 'topic')
    context_list = 'article_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

class ArticleDetail(SelectRelatedMixin, LoginRequiredMixin, DetailView):
    model = Article
    select_related = ('created_by', 'topic')
    slug_field = 'article_name'
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ArticleCreate(SelectRelatedMixin, LoginRequiredMixin, CreateView):
    template_name = 'article_form.html'
    form_class = ArticleForm
    model = Article

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user.user_profile
        topic = get_object_or_404(Topic, topic_name=self.kwargs.get('slug'))
        self.object.topic = topic
        self.object.save()
        return super().form_valid(form)


    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:topic_detail',kwargs={'slug':self.kwargs.get('slug')})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = get_object_or_404(Topic, topic_name=self.kwargs.get('slug'))
        context['topic'] = topic
        return context


class DeleteArticle(SelectRelatedMixin, LoginRequiredMixin, DeleteView):
    model = Article
    select_related = ('userprofile', 'topic')
    success_url = reverse_lazy('articles:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Article Deleted')
        return super().delete(*args, **kwargs)