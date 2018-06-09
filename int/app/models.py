from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User


class comments_feed(models.Model):
    name = models.CharField(max_length=264)
    idea = models.CharField(max_length=264)
  

class buy_model(models.Model):
    name = models.CharField(max_length=100)
    product_name = models.CharField(max_length = 150)
    email = models.EmailField()
    address_Line1 = models.CharField(max_length=150)
    address_Line2 = models.CharField(max_length=150)
    city = models.CharField(max_length=164)
    phone_no = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999,"Please Enter a Valid Phone Number")])
    country = models.CharField(max_length=164)

class foot_com(models.Model):
    com_foo = models.CharField(max_length=264)
