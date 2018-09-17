from django.shortcuts import render
from .forms import userForm, profileForm, imageForm


def indexView(request):
    return render(request, 'index.html')


def registerView(request):
    registered = False

    if request.method == 'POST':
        user_form = userForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

        else:
            print(user_form.errors)
    else:
        user_form = userForm()

    context = {
        'user_form': user_form,
        'registered': registered,
    }

    return render(request, 'registerPage.html', context)


def extraView(request):
    submitted = False

    if request.method == 'POST':
        extra_form = profileForm(data=request.POST)
        image_form = imageForm(data=request.POST)

        if extra_form.is_valid() and image_form.is_valid():
            user = extra_form.save()
            user.save()

            profile = image_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            submitted = True

        else:
            print(extra_form.errors, image_form.errors)
    else:
        extra_form = profileForm()
        image_form = imageForm()

    context = {
        'extra_form': extra_form,
        'image_form': image_form,
        'submitted': submitted,
    }

    return render(request, 'submitThis.html', context)
