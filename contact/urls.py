from django.urls import path
from . import views

urlpatterns = [
    path("contacts/", views.Contacts.as_view())
]






