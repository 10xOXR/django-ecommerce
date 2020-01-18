from django.urls import path, include
from accounts.views import index, logout, login, registration, user_profile
from accounts import urls_reset

urlpatterns = [
    path("logout/", logout, name="logout"),
    path("register/", registration, name="registration"),
    path("profile/", user_profile, name="profile"),
    path("password-reset/", include(urls_reset)),
    path("login/", login, name="login"),
]
