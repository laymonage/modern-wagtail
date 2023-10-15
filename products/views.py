from django.shortcuts import get_object_or_404, render

from products.models import Product


# Create your views here.
def index(request):
    products = Product.objects.filter(live=True)
    return render(request, "products/index.html", {"products": products})


def detail(request, pk):
    product = get_object_or_404(Product.objects.filter(live=True), pk=pk)
    return render(request, "products/detail.html", {"product": product})
