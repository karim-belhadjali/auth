from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from . import backend
from .decorators import unauthenticated_user, allowed_users
from .forms import CreateUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required


# Create your views here.
@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('full_name')
            messages.success(request, 'Account was created for ' + username)
            return redirect('loginPage')
        else:
            variables = {
                'form': form
            }
            return render(request, 'authtest/register.html', variables)

    stuff_for_frontend = {
        'form': form
    }
    return render(request, 'authtest/register.html', stuff_for_frontend)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def home(request):
    print(request.user)
    return render(request, 'authtest/home.html')


def logoutUser(request):
    logout(request)
    return redirect('loginPage')


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'authtest/login.html', context)
