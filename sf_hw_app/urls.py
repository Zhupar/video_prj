from django.urls import path, include
from .views import *




urlpatterns = [
    path('', index),
    path('search/', Search.as_view()),
    # path('', index),

]
