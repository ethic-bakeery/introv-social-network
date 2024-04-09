from django.urls import path
from .import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('about', views.about, name='about'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('google_register', views.google_register, name='google_register'),
    path('facebook_register', views.facebook_register, name='facebook_register'),
    path('forget_password', views.forget_password, name='forget_password'),
    path('blank', views.blank, name='blank'),
    path('not_found', views.not_found, name='not_found'),
]

