from django.db import models

class comments_feed(models.Model):
    name = models.CharField(max_length=264)
    comment = models.CharField(max_length=264)
