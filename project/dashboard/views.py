from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Product, Order
from .forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .decorators import auth_users, allowed_users


@login_required(login_url="user-login")
def index(request):
    return render(request, "dashboard/index.html")

@login_required(login_url="user-login")
def staff(request):
    return render(request, "dashboard/staff.html")

@login_required(login_url="user-login")
def products(request):

    all_products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-products')
    else:
        form = ProductForm()

    context = {
        "all_products" : all_products,
        "form" :form,
    }

    return render(request, "dashboard/products.html",context)

@login_required(login_url="user-login")
def order(request):
    return render(request, "dashboard/order.html")