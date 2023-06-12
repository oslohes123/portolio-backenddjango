from django.contrib import admin
from django.urls import path, include
from .views import testingView

urlpatterns = [
    path('testing', testingView.as_view())
]
