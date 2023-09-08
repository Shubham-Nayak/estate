from . import views
from django.urls import path

urlpatterns = [
    path('login', views.index,name='login'),
    path('register', views.register,name='register'),
    path('logout', views.logout,name='logout'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('', views.index,name='login'),




]
