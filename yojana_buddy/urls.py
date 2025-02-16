from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("login"), name="home"),  # ✅ Redirect home to login page
    path("admin/", admin.site.urls),
    path("chatbot/", include("chatbot.urls")),
    path("accounts/", include("accounts.urls")),
]
