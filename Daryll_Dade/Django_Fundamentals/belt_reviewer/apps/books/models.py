# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_and_reg.models import User

class BookManager(models.Manager):
    def createBook(self, form_data):
        if form_data['choice']:
            author = form_data['choice']
        else:
            author = form_data['author']

        book = Book.objects.create(
            title = form_data['title'],
            choice = form_data['choice'],
            author = form_data['author'],
            review = form_data['review'],
            rating = form_data['rating'],
            uploader = request.session['user_id'],
        )
        return book

class Book(models.Model):
    title=models.CharField(max_length=255)
    choice=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    review=models.TextField(max_length=2000)
    rating=models.SmallIntegerField(default=0)
    uploader=models.ManyToManyField(User, related_name="books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()
