from django.urls import path

from . import views

urlpatterns = [
    path("photos/", views.photos, name="photos"),
    path("photos/<str:photo_id>/", views.photo, name="photo"),  # Cambiado a str
    path("", views.index, name="index"),
]
