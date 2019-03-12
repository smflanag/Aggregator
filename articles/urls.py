from django.conf.urls import url, include
from django.urls import path, reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter

from articles import views as article_views
from accounts import views as account_views
from groups import views as group_views
from articles.models import Article

app_name = 'articles'

router = DefaultRouter()
router.register('articles', article_views.ArticleViewSet, 'articles')
router.register('topics', group_views.TopicViewSet, 'topics')

urlpatterns = [
    url(r'^topic/(?P<slug>[-\w]+)/create_article/$', article_views.ArticleCreate.as_view(), name='article_form'),
    url(r'^article/(?P<slug>[-\w]+)/upvote', article_views.Upvote.as_view(), name='upvote'),
    url(r'^article/(?P<slug>[-\w]+)/downvote', article_views.Downvote.as_view(), name='downvote'),
    # url(r'^article/(?P<slug>[-\w]+)/comment', article_views.AddComment.as_view(), name='comment_form'),
    url(r'^article/(?P<slug>[-\w]+)', article_views.ArticleDetail.as_view(), name='article_detail'),

    path('articles/', account_views.article_list),

    url(r'^article/(?P<slug>[-\w]+)/delete', article_views.ArticleDelete.as_view(), name='article_delete'),


    path(r'articles/<int:pk>/upvote', article_views.js_upvoting),
    path(r'articles/<int:pk>/downvote', article_views.js_downvoting),
    path(r'articles/<int:pk>/comment', article_views.js_commenting),

    url(r'^api/', include(router.urls)),
    ]