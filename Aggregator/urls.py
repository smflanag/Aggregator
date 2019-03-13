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
from django.urls import include, path, re_path
from accounts import views as account_views
from articles import views as article_views
from groups import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$',article_views.ArticlesReact.as_view(),name='home'),
    # path('',article_views.ArticlesReact.as_view(),name='articles'),
    url(r'^', include('accounts.urls', namespace="accounts")),
    path('', include('django.contrib.auth.urls')),
    url(r'admin/', admin.site.urls),

    url(r'^', include('articles.urls', namespace="articles")),
    url(r'^', include('groups.urls', namespace="groups")),
    path('rest-auth/', include('rest_auth.urls')),
    re_path('.*', TemplateView.as_view(template_name='index.html')),
    ]

urlpatterns += staticfiles_urlpatterns()