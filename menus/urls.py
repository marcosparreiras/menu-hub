from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_restaurants, name="home"),
    path("edit/<int:restaurante_id>", views.edit_restaurants, name="edit"),
    path("delete/<int:restaurante_id>", views.delete_restaurant, name="delete"),
]
