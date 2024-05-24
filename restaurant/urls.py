from django.urls import path

from restaurant.views import (
    RestaurantListCreateView,
    MenuListCreateView,
    DishListCreateView,
)

urlpatterns = [
    path(
        "",
        RestaurantListCreateView.as_view(),
        name="restaurant-list-create",
    ),
    path(
        "menus/",
        MenuListCreateView.as_view(),
        name="menu-list-create",
    ),
    path(
        "dishes/",
        DishListCreateView.as_view(),
        name="dish-list-create",
    ),

]

app_name = "restaurant"
