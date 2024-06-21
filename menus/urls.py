from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_restaurants, name="home"),
]
