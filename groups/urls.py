from django.conf.urls import url

from groups import views as group_views
from groups.models import Topic

app_name = 'groups'

urlpatterns = [
    url(r'topic/$', group_views.TopicList.as_view(), name='topic_list'),
    url(r'^topic/(?P<slug>[-\w]+)/$', group_views.TopicDetails.as_view(), name='topic_detail'),
    url(r'topic_create/$', group_views.TopicCreate.as_view(), name='new_topic'),
    ]