from django.urls import path
from .import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('about', views.about, name='about'),
    path('forget_password', views.forget_password, name='forget_password'),
    path('blank', views.blank, name='blank'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('messages/', views.messages, name='messages'),
    path('modal/', views.modal, name='modal'),
    path('newsfeed/', views.newsfeed, name='newsfeed'),
    path('profile/', views.profile, name='profile'),
    path('set_billing/', views.set_billing, name='set_billing'),
    path('set_fingerprint/', views.set_fingerprint, name='set_fingerprint'),
    path('set_location/', views.set_location, name='set_location'),
    path('set_contact/', views.set_contact, name='set_contact'),
    path('set_password/', views.set_password, name='set_password'),
    path('settings/', views.settings, name='settings'),
    path('widgets/', views.widgets, name='widgets'),
    path('components/', views.components, name='components'),
    path('friends/', views.friends, name='friends'),
    path('groups/', views.groups, name='groups'),
]
