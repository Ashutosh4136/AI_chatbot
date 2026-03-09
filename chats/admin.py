from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ChatSession, Message

admin.site.register(ChatSession)
admin.site.register(Message)