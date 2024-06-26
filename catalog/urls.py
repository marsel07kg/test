from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.ProductListView.as_view()),
    path("catalog/<int:id>/", views.ProductsDetailView.as_view()),
    path("rewiews/", views.RewiewsCreateView.as_view())
]