import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http import request, HttpRequest
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views import generic
from django.views.generic.detail import SingleObjectMixin
from django.core.exceptions import ObjectDoesNotExist

from articles.models import Article
from groups import models
from groups.forms import TopicForm
from groups.models import Topic
#from braces.views import SelectRelatedMixin, LoginRequiredMixin
from braces.views import SelectRelatedMixin

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
