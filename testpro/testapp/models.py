from django.db import models
from django.contrib.auth.models import User

class usermodel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    site = models.URLField()
    profile_pic = models.ImageField(upload_to = 'profile_pic',blank = True)
