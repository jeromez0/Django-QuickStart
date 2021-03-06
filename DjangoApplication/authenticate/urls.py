from django.urls import path, include
from . import views


urlpatterns = [
    path('loginPage', views.loginPage, name='loginPage'),
    path('logoutPage', views.logoutPage, name='logoutPage'),
    path('register', views.register_user, name='register'),
    path('edit_profile', views.edit_profile, name = 'edit_profile'),
]
