from django.shortcuts import render
from django.views.generic import View,TemplateView
from .forms import UserForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings

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

def sending_mail(request):
    user1 = User.objects.all()
    subject = "Thank You For Subscribing"
    from_email = settings.EMAIL_HOST_USER
    to_email = [user1.email]
    signup_message = "Welcome To DA-Hobbies DIY .... Thanks For Subscribing......We'll Be in-touch With You!"
    send_mail(subject=subject,from_email=from_email,recipient_list=to_email,message=signup_message,fail_silently=False)

    return render(request,'email.html')
