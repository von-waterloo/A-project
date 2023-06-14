from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from chat.forms import AuthForms


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


class MyLoginView(LoginView):
    template_name = 'chat/login.html'
    redirect_authenticated_user = False
class MyLogoutView(LogoutView):
    next_page = 'chat/'




