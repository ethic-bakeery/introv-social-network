from django.urls import path
from .import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('logout', views.user_logout, name='logout'),
    path('login', views.user_login, name='login'),
    path('about', views.about, name='about'),
    path('dashboard', views.dashboard, name='dashboard')
]
