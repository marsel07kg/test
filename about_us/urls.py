from django.urls import path
from . import views

urlpatterns = [
    path("about_us/", views.Shop.as_view()),
]