from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from . import models

class Contacts(generic.ListView):
    template_name = 'contact/contact.html'
    context_object_name = 'contact_list'
    model = models.Contact

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')
# Create your views here.
