from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("socials/", views.socials, name="socials"),
]
