from django.shortcuts import render
from .models import Product
def products(req):
    myproduct = Product.objects.all().values()
    context = {
    'myproduct': myproduct,
    }
    return render(req,"products/products.html",context)