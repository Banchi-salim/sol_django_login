from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.connect_wallet, name="connect"),
    path("/success", views.wallet_success, name="wallet_success"),
]