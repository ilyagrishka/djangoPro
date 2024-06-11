from msilib.schema import ListView, DetailView, CreateView
from django.shortcuts import render, get_object_or_404

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreate(CreateView):
    model = Product
    fields = ("name", "description", "price")
    success_url = reverse_lazy("products:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "price")
    success_url = reverse_lazy("products:product_list")

    def get_success_url(self):
        return reverse_lazy("products:products_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(deleteView):
    model = Product
    success_url = reverse_lazy("products:product_list")
