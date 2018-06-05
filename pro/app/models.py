from django.db import models

class comments_feed(models.Model):
    name = models.CharField(max_length=264)
    idea = models.CharField(max_length=264)

class user_feed(models.Model):
    post_name = models.CharField(max_length=70)
    rev = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()

