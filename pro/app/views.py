from django.shortcuts import render
from .forms import userform,profileform

def index(request):
    return render(request,'app/index.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_model = profileform(data=request.POST)
        user_form = userform(data=request.POST)

        if user_model.is_valid() and user_form.is_valid():
            user = user_model.save()
            user.set_password(user.password)
            user.save()

            profile = user_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered = True

        else:
            print(user_form.errors,user_model.errors)        

    else:
        user_model = profileform()
        user_form = userform()

    context = {
        'user_model':user_model,
        'user_form':user_form,
        'registered':registered,
    }            

    return render(request,'app/register.html',context)

    
