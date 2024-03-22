from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


def home(req):
    # Check to see if logging in
    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]

        # Authenticate
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            messages.success(req, "You have been logged in")
            return redirect("home")
        else:
            messages.error(req, "Fail logged in")
            return redirect("home")
    else:
        return render(req, "home.html", {})


# def login_user(req):
#     pass


def logout_user(req):
    logout(req)
    messages.success(req, "You have been logged out...")
    return redirect("home")


def register_user(req):
    if req.method == "POST":
        form = SignUpForm(req.POST)
        if form.is_valid():
            form.save()
            # Authen and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(req, user)
            messages.success(req, "Successfully Registered")
            return redirect("home")
    else:
        form = SignUpForm()
        return render(req, "register.html", {"form": form})

    return render(req, "register.html", {"form": form})
