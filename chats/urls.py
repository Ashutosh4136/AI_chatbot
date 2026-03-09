from django.urls import path
from .views import *

urlpatterns = [
    path("chat/", chat_page, name="chat"),
    path("new/", new_chat, name="new_chat"),
    path("chat/<int:session_id>/", chat_page, name="chat_session"),
    path("delete/<int:session_id>/", delete_chat, name="delete_chat"),
]