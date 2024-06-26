from django.shortcuts import render, get_object_or_404
from django.views import generic

from . import models, forms

class ProductsDetailView(generic.DetailView):
    template_name = 'catalog/products_detail.html'
    context_object_name = 'products_detail'

    def get_object(self, **kwargs):
        product = self.kwargs.get("id")
        return get_object_or_404(models.Product, id=product)

class ProductListView(generic.ListView):
    template_name = 'catalog/product_list.html'
    context_object_name = 'product_list'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')

class RewiewsCreateView(generic.CreateView):
    template_name = 'catalog/rewiew_create.html'
    form_class = forms.RewiewsForm
    success_url = "/catalog/"

    def form_valid(self, form):
        return super(RewiewsCreateView, self).form_valid(form=form)
# Create your views here.
