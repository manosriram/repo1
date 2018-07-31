from django.db import models


vote_choices = [
    ('steve jobs','STEVE JOBS'),
    ('bill gates','BILL GATES'),
]

class vote_model(models.Model):
    entrep = models.CharField(max_length=15,choices = vote_choices,default="Select Here.")


class Counter(models.Model):
    count = models.IntegerField(default=0)
    page = models.IntegerField()


print(vote_choices[0])     