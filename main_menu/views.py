from django.shortcuts import render
from django.views import generic
from . import models





class MainMenuView(generic.ListView):
    template_name = 'main_menu/main_menu.html'
    context_object_name = 'menu_list'
    model = models.Slogan
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video_url'] = models.Video.objects.order_by('-id')
        context['popular_product'] = models.Product.objects.order_by('-id')

        return context
    def get_queryset(self):
        return self.model.objects.all()
# Create your views here.
