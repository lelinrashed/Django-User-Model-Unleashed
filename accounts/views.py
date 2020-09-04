from accounts.forms import UserCreationForm, UserLoginForm
from django.contrib.auth import login, get_user_model, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

User = get_user_model()

def home(request):
    return render(request, "accounts/home.html")


def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        print("User created")
        return HttpResponseRedirect("/login/")
    return render(request, "accounts/register.html", {"form": form})


def user_login(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        # form.save()
        user_obj = form.cleaned_data.get("user_obj")
        # user_obj = User.objects.get(username__iexact=username)
        login(request, user_obj)
        print("User Login")
        return HttpResponseRedirect("/")
    return render(request, "accounts/login.html", {"form": form})


def user_logout(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect("/")
