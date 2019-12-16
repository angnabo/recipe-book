from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

from recipeApp.users.forms import UserLoginForm, UserSignupForm


def index(request):
    form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})


def signUp(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.email
            password = form.password1
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserSignupForm()
    return render(request, 'users/signup.html', {'form': form})


def logIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/recipes')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
