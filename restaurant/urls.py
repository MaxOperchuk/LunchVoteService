from django.urls import path

from restaurant.views import (
    RestaurantListCreateView,
    MenuListCreateView,
)


urlpatterns = [
    path(
        "",
        RestaurantListCreateView.as_view(),
        name="restaurant-list",
    ),
    path(
        "menus/",
        MenuListCreateView.as_view(),
        name="menu-list-create",
    ),
]

app_name = "restaurant"
