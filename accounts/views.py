from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# def signup_view(request):
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Log user in immediately after signup
#             return redirect("home")
#     else:
#         form = CustomUserCreationForm()
#     return render(request, "accounts/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = CustomAuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")


from django.shortcuts import render, redirect
from .forms import VolunteerForm

def volunteer_view(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "accounts/volunteer_success.html")
    else:
        form = VolunteerForm()
    return render(request, "accounts/volunteer.html", {"form": form})

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # send to homepage after signup
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})
