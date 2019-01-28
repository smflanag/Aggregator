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
from django.urls import include, path
from accounts import views as account_views
from articles import views as article_views
from articles import api as article_api_views
from rest_framework.authtoken import views as auth_token_views
from groups import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', article_api_views.ArticleViewSet)


urlpatterns = [
    url(r'^$',account_views.Homepage,name='home'),
    url(r'^', include('accounts.urls', namespace="accounts")),
    path('', include('django.contrib.auth.urls')),
    url(r'admin/', admin.site.urls),
    url(r'^api-token-auth/', auth_token_views.obtain_auth_token),
    url(r'^api/auth/register/$', article_api_views.RegistrationAPI.as_view()),
    url(r'^api/', include(router.urls)),



    url(r'^', include('articles.urls', namespace="articles")),
    url(r'^', include('groups.urls', namespace="groups")),
    path('rest-auth/', include('rest_auth.urls')),
    ]

urlpatterns += staticfiles_urlpatterns()