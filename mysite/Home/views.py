from django.shortcuts import render
from .models import *
from . import models

# Create your views here.

def Login(request): 
    context = {
               'form' : models.Login(),
               }
    if request.method == 'POST':
        if Account.objects.filter(username__exact=request.POST['username']):
            _login_ = Account.objects.filter(username__exact=request.POST['username'])[0]
            if _login_.password == request.POST['password']:
                request.session['ID'] = _login_.id
                return render(request, 
                              'Home/Single_notification.html', 
                              {
                                  'title' : 'Log in',
                                  'Notification_title' : 'Log in successfully',
                              })

        context['Notification'] = 'Username or Password is wrong'

    return render(request, 'Home/Login.html', context)


def Signin(request):
    context = {
                'form' : Signup(),
        }
    if request.method == 'POST':
        if Account.objects.filter(username__exact=request.POST['username']):
            context['Notification'] = 'This username existed'
        else:
            Signup(request.POST).save() 
            request.session['ID'] = Account.objects.filter(username__exact=request.POST['username'])[0].id
            return render(request, 
                              'Home/Single_notification.html', 
                              {
                                  'title' : 'Sign up',
                                  'Notification_title' : 'Sign up successfully',
                              })
                       
    return render(request, 'Home/Signin.html', context)


def home(request):
    return render(request, 'Home/home.html')


def contact(request):
    return render(request, 'Home/contact.html')
