from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from groups import views as group_views
from groups.models import Topic

app_name = 'groups'

urlpatterns = [
    url(r'topic/$', group_views.TopicList.as_view(), name='topic_list'),
    url(r'^topic/(?P<slug>[-\w]+)/$', group_views.TopicDetails.as_view(), name='topic_detail'),
    #url(r'^topics/$',group_views.js_topic_list),

    # path('topics/', group_views.TopicReact.as_view(), name='topicReact'),

    url(r'^topics/(?P<id>[0-9]+)/$', group_views.APITopicDetail.as_view()),
    url(r'topic_create/$', group_views.TopicCreate.as_view(), name='new_topic'),
    url(r'topic_delete/(?P<slug>[-\w]+)', group_views.TopicDelete.as_view(), name='topic_delete'),
    url(r'join/(?P<slug>[-\w]+)/$', group_views.JoinTopic.as_view(),name='join'),
    url(r'leave/(?P<slug>[-\w]+)/$', group_views.LeaveTopic.as_view(),name='leave'),



    url(r'^topic_detail/(?P<id>[0-9]+)$', group_views.js_topic_detail),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)