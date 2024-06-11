from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ProductCreateView

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_details"),
    path("products/create", ProductCreateView.as_view(), name="products_create"),
    path("products/<int:pk>/update", ProductUpdateView.as_view(), name="products_update"),
    path("products/<int:pk>/delete", ProductDeleteView.as_view(), name="products_delete")


]
