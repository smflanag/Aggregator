
from django.db import models
from django.template.defaultfilters import slugify

from accounts.models import UserProfile
from groups.models import Topic


class Article(models.Model):
    created_by = models.ForeignKey(UserProfile, related_name='articles', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    article_name = models.CharField(max_length=126)
    article_content = models.TextField()
    message_html = models.TextField(editable=False, default='')
    topic = models.ForeignKey(Topic, related_name='article', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, default=slugify(article_name))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.article_name)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.article_name

    def get_absolute_url(self):
        return u'/article/%s' % slugify(self.article_name)


class Vote(models.Model):
    voter = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    value = models.IntegerField()
    time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('voter', 'article')

    def __str__(self):
        return self.article.article_name + ' , ' + self.voter.user.username + ' , ' +  str(self.value)


class Comment(models.Model):
    commenter = models.ForeignKey(UserProfile, on_delete=models.CASCADE) ##remove null=True
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_body = models.TextField()
    message_html = models.TextField(editable=False, default='')
    time = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.article.article_name + ' , ' + self.commenter.user.username

    def get_absolute_url(self):
        return u'/article/%s' % slugify(self.article)


