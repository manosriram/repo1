from django.shortcuts import render
from .forms import register_form
from django.views.generic import View,TemplateView
from django.contrib.auth.models import User

# forms
from .forms import post_form

# models 
from .models import post

# http redirecting imports
from django.http import HttpResponse,HttpResponseRedirect

# login credentials
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

#reverse 
from django.urls import reverse

class logged_view(TemplateView):
    template_name = 'logged_in.html'



def indexView(request):
    grab = post.objects.all()

    context = {
        'grab':grab,
    }
    return render(request,'index.html',context)



def register_view(request):
    registered = False

    if request.method == 'POST':

        user_form = register_form(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = register_form()

    context = {
        'user_form':user_form,
        'registered':registered,
    }     

    return render(request,'register.html',context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('logged'))
            else:
                return HttpResponse("Account Not Active..Please Register and Then Try Again...")    

        else:
            print("Login Failed...Please Try Again..")        
    else:   
        return render(request,'login.html') 

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def post_view(request):
    posted = False
    if request.method == 'POST':
        user_form = post_form(data=request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            posted = True

        else:
            print(user_form.errors)        

    else:
        user_form = post_form()
    context = {
        'user_form':user_form,
        'posted':posted,
    }    

    return render(request,'post.html',context)

def post_view1(request):
    grab = post.objects.all()

    context = {
        'grab':grab,
    }
    return render(request,'profile.html',context)