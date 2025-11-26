from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from . import forms

# Create your views here.


def register(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        print(f"---------- {form} ----------")
        print("--------------")
        print(request.user)
        print("--------------")
        print(request.path)
        print("--------------")
        print(form.cleaned_data)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data["username"]
            messages.success(
                request,
                f"{username} registered successfully, login for whole experience",
            )
            return redirect("users:login")

    else:
        form = forms.UserRegisterForm()
    context = {"page_title": "register", "form": form}
    return render(request, "users/register.html", context)


@login_required
def profile(request):
    context = {}
    return render(request, "users/profile.html", context)
