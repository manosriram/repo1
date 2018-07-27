from django.db import models

vote_choices = (
    ('mark zuckerberg','MARK ZUCKERBERG'),
    ('steve jobs','STEVE JOBS'),
    ('jack ma','JACK MA'),
    ('elon musk','ELON MUSK'),
    ('warren buffet','WARREN BUFFET'),
)

class vote_model(models.Model):
    entrep = models.CharField(max_length=15,choices = vote_choices,default="Select Here.")

class Counter(models.Model):
    count = models.IntegerField(default=0)
    page = models.IntegerField()
    
