from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.PROTECT, related_name="sender")
    recipient = models.ForeignKey(User, on_delete=models.PROTECT, related_name="recipient")
    content = models.CharField(max_length=200, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
