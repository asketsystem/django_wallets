from django.apps import AppConfig
from django.conf.urls import url
from django.urls import path
from .views import register
app_name = "accounts"

urlpatterns = [
    path('register/', register, name="register"),
]

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
