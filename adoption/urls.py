from django.urls import path

from adoption import views


app_name = "adoption"

urlpatterns = [
    path("", views.index, name="index"),
    path("pets/<int:pet_id>/", views.pet_details, name="pet_details"),
]
