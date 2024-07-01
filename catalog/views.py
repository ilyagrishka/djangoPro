from audioop import reverse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, BlogNote, Version
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreate(CreateView, LoginRequiredMixin):
    model = Product
    fields = ("name", "description", "price")
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "price")
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse_lazy("catalog:products_detail", args=[self.kwargs.get("pk")])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = ProductFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


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
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, slug):
        if form.is_valid():
            new_blog = slug.save()
            new_blog.slug = slugify()
            new_blog.save()

        return super().form_valid(slug)


class BlogNoteUpdateView(UpdateView):
    model = BlogNote
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:products_detail", args=[self.kwargs.get("pk")])


class BlogNoteDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
