import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views import generic, View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.detail import SingleObjectMixin
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from articles.models import Article
from groups.forms import TopicForm
from groups.models import Topic
#from braces.views import SelectRelatedMixin, LoginRequiredMixin
from braces.views import SelectRelatedMixin
from groups.serializers import TopicListSerializer
from rest_framework import viewsets

# Create your views here.
from django.views.generic import DetailView, CreateView, ListView, DeleteView

class TopicCreate(CreateView):
    model = Topic
    form_class = TopicForm
    template_name = 'new_topic.html'
    slug_field = 'slug'


class TopicDetails(DetailView, SingleObjectMixin):
    model = Topic
    template_name = 'topic_detail.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic_id = get_object_or_404(Topic, slug=self.kwargs.get('slug')).id
        article_list = Article.objects.filter(topic_id=topic_id).order_by('-created_at')
        context['article_list'] = article_list
        return context

    def get_absolute_url(self):
        return reverse('topic_detail', kwargs={'slug': self.slug})


class TopicList(ListView):
    model = Topic
    context_list = "topic_list"
    template_name = 'topic_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_absolute_url(self):
        return reverse('topic_detail', kwargs={'slug': self.slug})



class JoinTopic(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:topic_detail', kwargs={'slug': kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        topic = get_object_or_404(Topic, slug=kwargs.get('slug'))
        try:
            topic.members.add(self.request.user)
        except IntegrityError:
            messages.warning(self.request,'Warning already a member')
        else:
            messages.success(self.request,'You are now a member')
        return super().get(request,*args,**kwargs)



class LeaveTopic(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:topic_detail',kwargs={'slug':kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        topic = get_object_or_404(Topic, slug=self.kwargs.get('slug'))
        try:
            member = topic.members.filter(
                id=self.request.user.id
            ).get()
        except ObjectDoesNotExist:
            logging.warning('a user tried to leave a topic of which they are not a member')
            messages.warning(self.request,'Sorry you are not in this topic')
        else:
            topic.members.remove(self.request.user)
            messages.success(self.request,'You have left the topic')
        return super().get(request,*args,**kwargs)


class TopicDelete(SelectRelatedMixin, LoginRequiredMixin, DeleteView):
    model = Topic
    select_related = (None,)
    slug_field = 'slug'
    template_name = 'topic_delete.html'
    success_url = reverse_lazy('home')

class APITopicList(APIView):
    """
    List all topics or create a new topic
    """
    def get(self,request,format=None):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics,many=True)
        return Response(serializer.data)

    def post(self, request,format=None):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TopicReact(View):
    title = "Topics"
    template = 'topics.html'

    def get(self, request):
        topics = list(Topic.objects.values('id', 'topic_name'))

        context = {
            'topic_name': self.title,
            'props': topics,
        }

        return render(request, self.template, context)


@csrf_exempt
@api_view(['GET',])
def js_topic_list(request):
    if request.method == 'GET':
        topics = Topic.objects.all()
        yourdata =[]
        for topic in topics:
            topic_id = topic.id
            topic_name = topic.topic_name
            members = topic.members.filter(topic=topic_id)
            articles = Article.objects.filter(topic_id=topic_id).count()
            yourdata.append(
                {"id":topic_id,
                 "topic_name":topic_name,
                 "articles":articles,
                "members":members})
        serializer=[]
        for data_thing in yourdata:
            serializer.append(TopicListSerializer(data_thing).data)
    return Response(serializer)


from articles.serializers import ArticleSerializer, TopicSerializer


@csrf_exempt
@api_view(['GET',])
def js_topic_detail(request,id):
    if request.method == 'GET':
        topic_id = id
        articles = Article.objects.filter(topic_id=topic_id).order_by('-created_at')
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)


"""
    Retrieve, update or delete a topic
"""
class APITopicDetail(APIView):

    def get_object(self,id):
        try:
            return Topic.objects.get(id=id)
        except Topic.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        topic = self.get_object(id)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        topic = self.get_object(id)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)

    def delete(self, request,id,format=None):
        topic = self.get_object(id)
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TopicViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Topic.objects.all()
    serializer_class = TopicSerializer

    def perform_create(self, serializer):
        serializer.save()
