from django.urls import path, register_converter
from . import views
from .converters import DateConverter

register_converter(DateConverter, "date")
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("book/", views.book, name="book"),
    path("reservations/", views.reservations, name="reservations"),
    path("menu/", views.menu, name="menu"),
    path("menu_item/<int:pk>/", views.display_menu_item, name="menu_item"),
    path("bookings/", views.bookings, name="bookings"),
]
