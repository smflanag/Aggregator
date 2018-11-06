from django.contrib.auth.models import User
from django.db import models
from django.contrib import auth

# Create your models here.
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify

from groups.models import Topic


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    topics = models.ManyToManyField(Topic)
    # slug = models.SlugField(unique=True, default=user)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.user)
    #     super(UserProfile, self).save(*args, **kwargs)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)

    def __str__(self):
        return self.user.username


    def get_absolute_url(self):
        return u'/profile/%s' % self.user