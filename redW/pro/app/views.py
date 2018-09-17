from django.shortcuts import render
from .forms import userForm, profileForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import userInfo


def indexView(request):
    return render(request, "index.html")


def registerView(request):
    registered = False

    if request.method == "POST":
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

    context = {"user_form": user_form, "registered": registered}

    return render(request, "registerPage.html", context)


def grabView(request):
    grab = profileForm(data=request.POST)

    context = {"grab": grab}
    return render(request, "information.html", context)


def formView(request):
    submitted = False

    if request.method == "POST":
        profile_form = profileForm(data=request.POST)

        if profile_form.is_valid():
            user1 = profile_form.save()
            user1.save()

            profile = profile_form.save(commit=False)
            profile.user1 = user1

            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]
            profile.save()

            submitted = True

        else:
            print(profile_form.errors)
    else:
        profile_form = profileForm()

    context = {"profile_form": profile_form, "submitted": submitted}

    return render(request, "submitThis.html", context)


def loginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))

            else:
                return HttpResponse("Account Not Active")
        else:
            print("Login Failed..")

    else:
        return render(request, "login.html")


@login_required
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

