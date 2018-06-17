from django.db import models

class post(models.Model):
    text = models.CharField(max_length=1064)
    nick_name = models.CharField(max_length=10)

