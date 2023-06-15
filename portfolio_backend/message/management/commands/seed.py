from django.core.management.base import BaseCommand
from message.MessageFactory import MessageFactory
import faker

class Command(BaseCommand):
    def _generate_posts(self,amount:int):            
        MessageFactory.create_batch(amount)
    
    def handle(self,*args,**kwargs):
        amount = kwargs.get('amount') or 10
        self._generate_posts(amount)


