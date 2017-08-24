# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt, re

#EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def validateRegistration(self, form_data):
        errors = []
        user = User.objects.filter(email = form_data['email'])

        if len(form_data['name']) == 0:
            errors.append("Name is required.")
        if len(form_data['alias']) == 0:
            errors.append("Alias is required.")
        if len(form_data['email']) == 0:
            errors.append("Email is required.")
        if len(form_data['password']) == 0:
            errors.append("password is required.")
        if len(form_data['pw_confirmation']) == 0:
            errors.append("pw_confirmation is required.")

        return errors

    def validateLogin(self, form_data):
        errors = []
        if len(form_data['email']) == 0:
            errors.append("Email is required.")
        if len(form_data['password']) == 0:
            errors.append("password is required.")

        return errors
        # if not EMAIL_REGEX.match(form_data['email']):
        #     errors.append('The email you entered is not in valid email format.')
        # else:
        #    errors.append('The email you entered is not in our database.')

        # if user:
        #     user = User.objects.filter(email = form_data['email']).first()
        #     password = str(form_data['password'])
        #     if bcrypt.checkpw(password, str(user.password)) == False:
        #         errors.append('The password you entered is invalid.')
        #     else:
        #         return user
        #
        # return errors


    def createUser(self, form_data):
        password = str(form_data['password'])
        hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt(10))
        user = User.objects.create(
            name = form_data['name'],
            alias = form_data['alias'],
            email = form_data['email'],
            password = hashed_pw
        )
        return user

    def currentUser(self, request):
        id= request.session['user_id']

        return User.objects.get(id=id)

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __str__(self):
        string_output = "id: {}  name: {} alias: {} email: {} password: {}"

        return string_output.format(
            self.id,
            self.name,
            self.alias,
            self.email,
            self.password,
        )
