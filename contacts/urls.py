from . import views
from django.urls import path

urlpatterns = [
    path('contact', views.index,name='contact'),

]
