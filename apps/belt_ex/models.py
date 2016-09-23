from __future__ import unicode_literals
from django.db import models
import datetime
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

class UserManager(models.Manager):
    def register(self, name, alias, email, password, passconf, dob):
        errors = []
        if len(name) < 2:
            errors.append('Name must be at least 2 characters')
        if not NAME_REGEX.match(name):
            errors.append('Name may only contain letters')
        if len(alias) < 2:
            errors.append('Alias must be at least 2 characters')
        if not NAME_REGEX.match(alias):
            errors.append('Alias may only contain letters')
        if not EMAIL_REGEX.match(email):
            errors.append('invalid email')
        if len(password) < 5:
            errors.append('Password must be at least 5 characters')
        if passconf != password:
            errors.append('Password confirmation must match password')
        if len(dob) <1:
            errors.append('must enter dob')
        if len(errors) > 0:
            return (errors, None)
        else:
            check_email = User.objects.filter(email = email.lower())
            if len(check_email) > 0:
                return(['Already in the system'], None)
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            User.objects.create(name = name,alias = alias,email = email,password = pw_hash, dob = dob)
            return (None, 'user')

    def login(self, email, password):
        user = User.objects.filter(email = email)
        if len(user) > 0:
            user = user[0]
            if bcrypt.hashpw(password.encode(), user.password.encode()) == user.password:
                return (None, user)
        return (['Wrong login'], None)


class User(models.Model):
    name = models.CharField(max_length=30)
    alias = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=200)
    dob = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()
    objects = models.Manager()

class Relationship(models.Model):
    user_id = models.ForeignKey(User, related_name = "user_relate")
    friend_id = models.ForeignKey(User, related_name = "friend_relate")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
