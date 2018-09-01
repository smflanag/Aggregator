from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Topic(models.Model):
    topic_name = models.CharField(max_length=126)
    topic_description = models.CharField(max_length=526,default='SOME STRING')
    slug = models.SlugField(unique=True)
    members = models.ManyToManyField(User)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.topic_name)
        super(Topic, self).save(*args, **kwargs)

    def __str__(self):
        return self.topic_name

    def get_absolute_url(self):
        return u'/topic/%s' % self.topic_name


