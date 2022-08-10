from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="user-login")
def index(request):
    return render(request, "dashboard/index.html")

@login_required(login_url="user-login")
def staff(request):
    return render(request, "dashboard/staff.html")

@login_required(login_url="user-login")
def products(request):

    all_products = Product.objects.all()

    context = {
        "all_products" : all_products
    }

    return render(request, "dashboard/products.html",context)
    
@login_required(login_url="user-login")
def order(request):
    return render(request, "dashboard/order.html")