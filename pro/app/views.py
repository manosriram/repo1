from django.shortcuts import render
from django.views.generic import View,TemplateView
from .forms import UserForm,comment_form,buy_form,com_form,register_form
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from .models import comments_feed,buy_model,foot_com
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate


class IndexView(TemplateView):
    template_name = 'index.html'
    
class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html' 

class Latest(TemplateView):
    template_name = 'latest.html'

class Allvid(TemplateView):
    template_name = 'all_vid.html'

def signup(request):
    signed = False
    if request.method == 'POST':
        signup_form = UserForm(data=request.POST)

        if signup_form.is_valid():
            user = signup_form.save()
            signed = True
            user.save()

        else:
            print(signup_form.errors)
    else:
        signup_form = UserForm()
       
        # subject = "Thank You For Subscribing"
        # from_email = settings.EMAIL_HOST_USER
        # to_email = [User.email]
        # signup_message = "Welcome To DA-Hobbies DIY .... Thanks For Subscribing......We'll Be in-touch With You!"
        # send_mail(subject=subject,from_email=from_email,recipient_list=to_email,message=signup_message,fail_silently=False)
      

    context = {
        'sign_up':signup_form,
        'signed':signed,
    }    
    return render(request,'contact.html',context)


def comment_view(request):
    commented = False

    if request.method == 'POST':
        feedback = comment_form(data = request.POST)

        if feedback.is_valid():
            user = feedback.save()
            commented = True
            user.save()

        else:
            print(feedback.errors)    
    else:
        feedback = comment_form()

    context = {
        'comment_section':feedback,
        'commented':commented,
    }    
    return render(request,'data.html',context)


def feedback_data(request):
    data = comments_feed.objects.all()
    context = {
        'data':data,
    }

    return render(request,'data.html',context)

def buy_view(request):
    signedup = False

    if request.method == 'POST':
        buy_now = buy_form(data = request.POST)

        if buy_now.is_valid():
            fill_in = buy_now.save()
            signedup = True
            fill_in.save()

        else:
            print(buy_now.errors)    
    else:
        buy_now = buy_form()

    context = {
        'fill':buy_now,
        'signedup':signedup,
    }            

    return render(request,'fill_up.html',context)


def bot_com(request):
    done = False

    if request.method == 'POST':

        sub_com = com_form(data = request.POST)

        if sub_com.is_valid():
            save_it = sub_com.save()
            done = True
            save_it.save()

        else:
            print(sub_com.errors)    

    else:
        sub_com = com_form()

    context = {
        'com_sec':sub_com,
        'done':done,
    }            
    return render(request,'index.html',context)

def register_view(request):
    registered = False

    if request.method == 'POST':
        user_form = register_form(data = request.POST)

        if user_form.is_valid():
            saved = user_form.save()
            saved.set_password(saved.password)
            registered = True
            saved.save()

        else:
            print(user_form.errors)    

    else:
        user_form = register_form()

    context = {
        'user_form':user_form,
        'registered':registered,
    }            

    return render(request,'register.html',context)



def user_login(request):
    logged = False

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active..Please Register and Then Try Again...")    

        else:
            print("Login Failed...Please Try Again..")        
    else:
        return render(request,'login.html')        



@login_required
def user_logout(request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))
    






            
