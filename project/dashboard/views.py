from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request, "dashboard/index.html")

def staff(request):
    return render(request, "dashboard/staff.html")

def products(request):

    all_products = Product.objects.all()

    context = {
        "all_products" : all_products
    }

    return render(request, "dashboard/products.html",context)

def order(request):
    return render(request, "dashboard/order.html")