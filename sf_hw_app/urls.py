from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.VideoList.as_view()),
    path('search/', views.Search.as_view()),

]
