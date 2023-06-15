from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('testing', TestingView.as_view())
]
