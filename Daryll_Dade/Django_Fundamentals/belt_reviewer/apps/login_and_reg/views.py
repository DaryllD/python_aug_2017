# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User


def flashErrors(request, errors):
    for error in errors:
        messages.error(request, error)

def index(request):
    print "in index method"

    return render(request, 'login_and_reg/index.html')

def login(request):
    if request.method == "POST":
        errors = User.objects.validateLogin(request.POST)
    #    print type(errors)

    #check if we got an array of errors or a User object and respond accordingly
    # if errors:
        flashErrors(request, errors)
    # else:
    #    Print user
        # user_id=user.id
    # if not errors:
    #     user = User.objects.filter(email = request.POST['email']).first()
    #     if user:
    #         password = str(request.POST['password'])
    #         user_password = str(user.password)
    #         hashed_pw = bcrypt.hashpw(password, userpassword)
    #         if hashed_pw == user.password:
    #             request.session['user_id'] = user.idea
    #         errors.append("Invalid account information")
    # flashErrors(request, errors)
        return render(request, 'login_and_reg/index.html')
#    return redirect('login_and_reg/index')

def register(request):
    print "Inside the register function"

    if request.method == "POST":
        errors = User.objects.validateRegistration(request.POST)
        flashErrors(request, errors)
        # if not errors:
        #     user = User.objects.createUser(request.POST)
        #     request.session['user_id'] = user.id
        #     return redirect('books/index')


        return render(request, 'login_and_reg/index.html')

def logout(request):
    request.session.flush()
    return redirect('/')
