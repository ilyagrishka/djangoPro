from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product, BlogNote
from django.urls import reverse_lazy


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
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "price")
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse_lazy("catalog:products_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class BlogNoteListView(ListView):
    model = BlogNote


class BlogNoteDetail(DetailView):
    model = BlogNote

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogNoteCreate(CreateView):
    model = BlogNote
    fields = ("name", "description",)
    success_url = reverse_lazy("catalog:product_list")


class BlogNoteUpdateView(UpdateView):
    model = BlogNote
    fields = ("name", "description",)
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse_lazy("catalog:products_detail", args=[self.kwargs.get("pk")])


class BlogNoteDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")

