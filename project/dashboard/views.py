from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Product, Order
from .forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .decorators import auth_users, allowed_users


@login_required(login_url="user-login")
def index(request):
    products = Product.objects.all()
    context={
        "products" :products
    }
    return render(request, "dashboard/index.html", context)

@login_required(login_url="user-login")
def staff(request):
    return render(request, "dashboard/staff.html")

@login_required(login_url="user-login")
def products(request):

    product = Product.objects.all()
    product_count = product.count()

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
        "product" : product,
        "form" :form,
        "product_count" : product_count
    }

    return render(request, "dashboard/products.html",context)

@login_required(login_url="user-login")
def order(request):
    return render(request, "dashboard/order.html")

def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-products')
    context = {
        'item': item
    }
    return render(request, 'dashboard/products_delete.html', context)

def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/products_edit.html', context)