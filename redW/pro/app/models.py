from django.db import models
from django.contrib.auth.models import User


class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    bio = models.CharField(max_length=300)
    interests = models.CharField(max_length=164)


class imageModel(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
