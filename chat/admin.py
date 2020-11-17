from django.contrib import admin

# Register your models here.
from chat.models import Message, Messagerecipient

admin.site.register(Message)
admin.site.register(Messagerecipient)