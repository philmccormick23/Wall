from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name is too short"
        elif not postData['first_name'].isalpha():
            errors["first_alpha"] = "No numbers allowed"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name is too short"
        elif not postData['last_name'].isalpha():
            errors["last_alpha"] = "No numbers allowed"
        if len(postData['email']) < 1:
            errors["email"] = "Email is too short"
        elif not EMAIL_REGEX.match(postData['email']):
            errors["email_valid"] = "Email wrong format"
        if len(postData['password']) < 8:
            errors["password"] = "Password is too short"
        if postData['password'] != postData['confirm']:
            errors["confirmation"] = "Your emails don't match"
        return errors



class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()


class Message(models.Model):
    message = models.CharField(max_length=1000)
    user = models.ForeignKey (User, related_name="post_message", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    message = models.ForeignKey (Message, related_name="message_message", on_delete=models.PROTECT)
    user = models.ForeignKey (User, related_name="message_user", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
