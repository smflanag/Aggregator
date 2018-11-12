from django.forms import ModelForm
from articles.models import Article, Comment


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ('article_name', 'article_content')


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('comment_body',)
