from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='message')
    message = models.TextField()
    sender = models.PositiveIntegerField(null=False) # 0: ownder, 1: bot
    datetime = models.DateTimeField(auto_now=True)
   
    @property
    def get_owner(self):
        return self.sender
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.message
    
class Note(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='notebook')
    message = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
   
    @property
    def get_owner(self):
        return self.sender
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.message