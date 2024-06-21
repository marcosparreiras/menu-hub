from django.shortcuts import render, redirect
from .models import Restaurant, MenuItem


def show_restaurants(request):
    restaurants = Restaurant.objects.order_by("name")
    context = {"restaurants": restaurants}
    return render(request, "menus/show_restaurants.html", context)


def edit_restaurants(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    if request.method == "POST":
        form_data = request.POST
        restaurant.name = form_data.get("name")
        restaurant.save()
        return redirect("/")

    context = {"restaurant": restaurant}
    return render(request, "menus/edit_restaurant.html", context)


def delete_restaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    if request.method == "POST":
        restaurant.delete()
        return redirect("/")
    context = {"restaurant": restaurant}
    return render(request, "menus/delete_restaurant.html", context)
