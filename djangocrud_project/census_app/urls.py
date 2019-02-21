# Create a route table for your application (urls.py)
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('readres/', views.readRes, name='readRes'),
    path('createres/', views.createRes, name='createRes'),
    path('updateres/', views.updateRes, name='updateRes'),
    path('deleteres/', views.deleteRes, name='deleteRes'),
]