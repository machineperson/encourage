from django.db import models
from django.utils import timezone

# Create your models here.
class Status(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    media_url = models.URLField(blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


class UserProfile(models.Model):
    user = models.ForeignKey('auth.User', unique=True)
    url = models.URLField(blank=True, null=True)
    bio = models.TextField()
    profile_picture_url = models.URLField(blank=True, null=True)
