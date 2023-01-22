from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile


def signup(request):
    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        access_token = request.POST.get('access_token')
        access_secret = request.POST.get('access_secret')
        password = request.POST.get('password')
        # confirm_password = request.POST.get('confirm_password')

        # check for unique username
        if User.objects.filter(username=username):
            return render(request, "authentication/signup.html", context={
                'is_error': True,
                'error': "Username is already in use"
            })

        # check for unique email
        if User.objects.filter(email=email):
            return render(request, "authentication/signup.html", context={
                'is_error': True,
                'error': "Email is already in use"
            })

        # create User object from form data
        user = User.objects.create_user(username, email, password)
        user.save()

        # create user Profile from form data
        profile = Profile.objects.create(
            ACCESS_TOKEN=access_token,
            ACCESS_SECRET=access_secret,
            user=user
        )
        profile.save()

        # redirect after signup
        return render(request, "index.html")

    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # create user object from form data
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # send user to page after valid signin
            # send username and password for automatic signin in new directory
            return redirect('home')
        else:
            return render(request, "authentication/signin.html", context={
                'is_error': True,
                'error': "Invalid credentials"
            })

    return render(request, "authentication/signin.html")


@login_required(login_url="/signin")
def signout(request):
    logout(request)
    return redirect('home')
