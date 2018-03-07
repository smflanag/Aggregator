"""Aggregator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another accountURLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include
from accounts import views
from groups import views as group_views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$',views.Homepage,name='home'),
    url(r'^users_only/$',views.LoggedInView.as_view(),name='users_only'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^signup/$',views.SignUp,name='signup'),
    url(r'profile/(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile),
    url(r'^accounts/$', include('django.contrib.auth.urls')),
    url(r'topic/$', group_views.TopicList.as_view(), name='topic_list'),
    url(r'^topic/(?P<slug>[-\w]+)$', group_views.TopicDetails.as_view()),
]
# url(r'^topic/(?P<pk>\d+)$', group_views.TopicDetails.as_view()),