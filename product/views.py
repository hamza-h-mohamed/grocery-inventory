from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Product


class ProductListView(ListView):
    
    model = Product
    template_name = 'product/home.html'

class ProductDetaiView(DetailView):

    model = Product

class ProductCreateView(CreateView):

    model = Product

class ProductDeleteView(DeleteView):

    model = Product