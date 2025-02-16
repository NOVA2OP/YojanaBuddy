from django.urls import path
from .views import login_page, signup_page, signup, login_view, logout_view

urlpatterns = [
    path("login/", login_page, name="login"),
    path("signup/", signup_page, name="signup"),
    path("login_api/", login_view, name="login_api"),
    path("signup_api/", signup, name="signup_api"),
    path("logout/", logout_view, name="logout"),
]
