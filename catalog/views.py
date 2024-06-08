from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def product_list(request):
    product = Product.object.all()
    context = {"products": product}
    return render(request, "product_list.html", context)


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_details.html", context)
