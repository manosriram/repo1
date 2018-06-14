from django.shortcuts import render
from .forms import register_form

def register_view(request):
    registered = False

    if request.method=='POST':
        user_form = register_form(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered=True

        else:
            print(user_form.errors)    

    else:
        user_form = register_form()
        
        
    context= {
        'user_form':user_form,
        'registered':registered,
        
    }
    return render(request,'index.html',context)  