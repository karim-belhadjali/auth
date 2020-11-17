from datetime import timezone, datetime

from django.db import models
# Create your models here.
from authtest.models import User


class Message(models.Model):
    subject = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    message_body = models.CharField(max_length=255, blank=True, null=False, default="")
    create_date = models.DateTimeField(auto_now_add=True)
    parent_message_id = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "Sender is:  " + self.creator.username + "  Subject is:  " + self.subject


class Messagerecipient(models.Model):
    recipient = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, null=True, on_delete=models.CASCADE)
    is_read = models.IntegerField(default=0)
    test = models.IntegerField(default=0)

    def __str__(self):
        return "Recipient is:  " + self.recipient.username + "  Subject is:  " + self.message.subject


class Chat(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='chats')
    created = models.DateTimeField(auto_now_add=True)
