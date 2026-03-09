from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ChatSession, Message
from .groq_client import get_ai_response
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def chat_page(request, session_id=None):

    sessions = ChatSession.objects.filter(user=request.user)

    session = None
    messages = []

    if session_id:
        session = get_object_or_404(ChatSession, id=session_id, user=request.user)
        messages = Message.objects.filter(session=session)

    if request.method == "POST":

        user_message = request.POST.get("message")

        if not session:
            session = ChatSession.objects.create(user=request.user, title=user_message[:30])

        Message.objects.create(
            session=session,
            role="user",
            content=user_message
        )

        ai_response = get_ai_response(user_message)

        Message.objects.create(
            session=session,
            role="assistant",
            content=ai_response
        )

        messages = Message.objects.filter(session=session)

    return render(request, "chats/chat.html", {
        "sessions": sessions,
        "messages": messages,
        "session": session
    })


@login_required
def new_chat(request):

    session = ChatSession.objects.create(user=request.user, title="New Chat")

    return redirect("chat_session", session_id=session.id)




@login_required
def delete_chat(request, session_id):

    session = get_object_or_404(ChatSession, id=session_id, user=request.user)

    session.delete()

    return redirect("chat")