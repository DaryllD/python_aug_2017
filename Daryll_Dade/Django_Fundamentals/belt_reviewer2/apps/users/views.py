# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User
import bcrypt


def flashErrors(request, errors):
    for error in errors:
        messages.error(request, error)

def index(request):
    print "in index method"




    return render(request, 'users/index.html')

def login(request):
    print "inside login method"
    if request.method == "POST":
        form_data = request.POST
        errors = User.objects.validateLogin(request.POST)
        flashErrors(request, errors)

        if not errors:
            user = User.objects.filter(email = form_data['email']).first()

            password = str(form_data['password'])

            if user:
                if bcrypt.checkpw(password, str(user.password)) == False:
                    errors.append('The password you entered is invalid.')
                    flashErrors(request,errors)
                    return redirect('/')
                else:
                    current_user = User.objects.currentUser(request)
                return redirect('/success')
            errors.append('User not in records. Please register')
            flashErrors(request,errors)
        return redirect('/')

def register(request):
    print "Inside the register function"

    if request.method == "POST":
        form_data = request.POST
        errors = User.objects.validateRegistration(request.POST)
        flashErrors(request, errors)
        if not errors:
            password = str(form_data['password'])
            hashed_pw= bcrypt.hashpw(password, bcrypt.gensalt())
            user = User.objects.createUser(request.POST)

            request.session['user_id']=user.id
            print request.session['user_id']
            return redirect('/success')

        return redirect('/')

def success(request):
    print "Inside Success Method"
    if 'user_id' in request.session:
        current_user = User.objects.currentUser(request) #['user_id']

        context ={
            'current_user': current_user,
        }
        return render(request, 'users/success.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')
