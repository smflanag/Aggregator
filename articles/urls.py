from django.conf.urls import url

from articles import views as article_views
from articles.models import Article

app_name = 'articles'

urlpatterns = [
    url(r'^topic/(?P<slug>[-\w]+)/create_article/$', article_views.ArticleCreate.as_view(), name='article_form'),
    url(r'^article/(?P<slug>[-\w]+)/upvote', article_views.Upvote.as_view(), name='upvote'),
    url(r'^article/(?P<slug>[-\w]+)/downvote', article_views.Downvote.as_view(), name='downvote'),
    url(r'^article/(?P<slug>[-\w]+)$', article_views.ArticleDetail.as_view(), name='article_detail'),


    ]