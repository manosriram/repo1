from django.shortcuts import render
from .forms import userform,usermodelform
from django import forms

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

