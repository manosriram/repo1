from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import vote_model,Counter
from .forms import vote_form
from django.db.models import F
from django.contrib.auth.models import User


def index(request):
    return render(request,'index1.html')


def vote_view(request):
    voted = False

    if request.method == 'POST':
        dropd = vote_form(request.POST)      

        if dropd.is_valid():
            userd1 = dropd.save()
            userd1.save()
            voted = True
            
        else:
            print(dropd.errors)    

    else:
        dropd = vote_form()

    context = {
        'voted':voted,
        'form':dropd,
    }    

    return render(request,'index.html',context)

def vote_list(request):
    grab = vote_model.objects.all()

    context = {
        'grab':grab,
    }

    return render(request,'list.html',context)
