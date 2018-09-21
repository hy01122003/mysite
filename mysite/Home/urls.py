from django.urls import path
from . import views

urlpatterns = [
    path('login', views.Login, name="url_Login"),   
    path('signin', views.Signin, name="url_Signup"),  
    path('', views.home, name='url_Home'),
    path('contact', views.contact, name='url_Contact'),    
]

