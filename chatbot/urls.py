from django.urls import path
from .views import chatbot_page, chatbot_api

urlpatterns = [
    path("", chatbot_page, name="chatbot_page"),  # Load HTML page
    path("api/", chatbot_api, name="chatbot_api"),  # API for chatbot
]
