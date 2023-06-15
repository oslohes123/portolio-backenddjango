from django.contrib import admin
from django.contrib.auth.models import User
from .models import Message

# Register your models here.
admin.register([User, Message])
