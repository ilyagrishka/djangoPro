from django.urls import path
from catalog.apps import MainConfig
from catalog.views import ProductListView, ProductDetail, ProductCreate, ProductUpdateView, ProductDeleteView, \
    BlogNoteListView, BlogNoteDetail, BlogNoteCreate, BlogNoteUpdateView, BlogNoteDeleteView

app_name = MainConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("catalog/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    path("catalog/create", ProductCreate.as_view(), name="products_create"),
    path("catalog/<int:pk>/update", ProductUpdateView.as_view(), name="products_update"),
    path("catalog/<int:pk>/delete", ProductDeleteView.as_view(), name="products_delete")
]
urlpatterns1 = [
    path("", BlogNoteListView.as_view(), name="blog_list"),
    path("catalog/<int:pk>/", BlogNoteDetail.as_view(), name="blog_detail"),
    path("catalog/create", BlogNoteCreate.as_view(), name="blog_create"),
    path("catalog/<int:pk>/update", BlogNoteUpdateView.as_view(), name="blog_update"),
    path("catalog/<int:pk>/delete", BlogNoteDeleteView.as_view(), name="blog_delete")
]

