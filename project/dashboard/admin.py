from re import A
from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category', 'quantity')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
# admin.site.unregister(Group)