from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.MainMenuView.as_view()),
]