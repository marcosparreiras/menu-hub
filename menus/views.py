from django.shortcuts import render
from .models import Restaurant, MenuItem


# Create your views here.
def show_restaurants(request):
    restaurants = Restaurant.objects.order_by("name")
    context = {"restaurants": restaurants}
    return render(request, "menus/show_restaurants.html", context)
