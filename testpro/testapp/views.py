from django.shortcuts import render
from .forms import userform,usermodelform
from django import forms
from .models import usermodel
from django.contrib.auth.models import User

# login imports
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return render(request,'testapp/thank.html')


def index(request):
    return render(request,'testapp/index.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = userform(data=request.POST)
        user_profile = usermodelform(data=request.POST)

        if user_form.is_valid() and user_profile.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_profile.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered  = True

        else:
            print(user_form.errors,user_profile.errors)

    else:
        user_form = userform()
        user_profile = usermodelform()


    context = {
        'user_form':user_form,
        'user_profile':user_profile,
        'registered':registered,
    }                    

    return render(request,'testapp/register.html',context)

def contact(request):
    return render(request,'testapp/contact.html')

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account Not Active..")    

        else:
            print("Invalid Login...")        

    else:
        return render(request,'testapp/login.html')        

def data_info(request):
    grabdata1 = usermodel.objects.all()
    grabdata2 = User.objects.all()
    
    context = {
        'grab1':grabdata1,
        'grab2':grabdata2,
      
    }
    return render(request,'testapp/info.html',context)
