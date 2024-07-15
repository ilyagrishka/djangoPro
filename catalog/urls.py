from django.urls import path
from catalog.apps import MainConfig
from catalog.views import ProductListView, ProductDetail, ProductCreate, ProductUpdateView, ProductDeleteView, \
    BlogNoteListView, BlogNoteDetail, BlogNoteCreate, BlogNoteUpdateView, BlogNoteDeleteView
from django.views.decorators.cache import cache_page

app_name = MainConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("catalog/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    path("catalog/create", ProductCreate.as_view(), name="products_create"),
    path("catalog/<int:pk>/update", ProductUpdateView.as_view(), name="products_update"),
    path("catalog/<int:pk>/delete", cache_page(60)(ProductDeleteView.as_view()), name="products_delete"),
    path("blog", BlogNoteListView.as_view(), name="blog_list"),
    path("blog/<int:pk>/", BlogNoteDetail.as_view(), name="blog_detail"),
    path("blog/create", BlogNoteCreate.as_view(), name="blog_create"),
    path("blog/<int:pk>/update", BlogNoteUpdateView.as_view(), name="blog_update"),
    path("blog/<int:pk>/delete", BlogNoteDeleteView.as_view(), name="blog_delete")
]
