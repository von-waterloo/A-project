from django.contrib import admin
from django.urls import include, path
from chat.views import *

urlpatterns = [
    path("chat/", include("chat.urls")),
    path("admin/", admin.site.urls),
    path('login/', MyLoginView.as_view(), name = "login"),
    path('', MyLogoutView.as_view(), name = 'logout')

]