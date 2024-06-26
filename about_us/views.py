from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from . import models

class Shop(generic.ListView):
    template_name = 'about_us/about_us.html'
    context_object_name = 'shop_list'
    model = models.Shop

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')

# Create your views here.
