from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.registerView, name = 'register'),
    path('login/', views.loginView, name = 'login'),
    path('logout/',views.logoutView, name = 'logout'),
    path('profile/',views.profileView, name = 'profile'),
]
