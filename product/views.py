from django.shortcuts import render, redirect

from product import models
from . models import product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView ,UpdateView, DeleteView
from django.urls import reverse_lazy

class ProductList( ListView):
    model = product
    context_object_name = 'product'
    template_name = 'product_list.html'
    
    
class  DetailViewProduct(DetailView):
    model = product
    context_object_name = 'product'
    template_name = 'product/product_detail.html'
        
    
    
class  CreateProduct(CreateView):
    model = product
    fields = '__all__'
    success_url = reverse_lazy('product-list')
    
class ProductUpdate(UpdateView):
    model = product
    fields = '__all__'
    success_url = reverse_lazy('post')


class DeleteView(DeleteView):
    model = product
    context_object_name = 'product'
    success_url = reverse_lazy('product-list')