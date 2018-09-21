from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.

class Signin(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Account(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    age  = models.CharField(max_length=3)
    email = models.CharField(max_length=40)

class Login(ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'password']
        labels = {
            'username': ('Username'),
            'password': ('Password'),
        }
        widgets = {
            'password' : forms.PasswordInput,            
        }

class Signup(ModelForm):
    class Meta:
        model = Account
        fields = ['username',
                  'password',
                  'name',
                  'age',
                  'email'
                  ]
        labels = {
            'username' : ('Username'),
            'password' : ('Password'),
            'name' : ('Name'),
            'age' : ('Age'),
            'email' : ('Email'),
            }
        widgets = {
            'password' : forms.PasswordInput,            
        }
