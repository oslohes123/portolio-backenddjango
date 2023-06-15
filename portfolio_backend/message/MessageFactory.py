import factory
from django.contrib.auth.models import User
from .models import Message
import faker
import random

fake = faker.Faker()
sender_name = fake.first_name()
reciever_name = fake.first_name()

class MessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Message

    if bool(random.getrandbits(1)):
        sender = User.objects.get_or_create(username=sender_name)[0]
        recipient = User.objects.get_or_create(username=reciever_name)[0]
    else:
        sender = User.objects.get_or_create(username=reciever_name)[0]
        recipient = User.objects.get_or_create(username=sender_name)[0]
        
    content = factory.Faker('sentence', nb_words=10)
