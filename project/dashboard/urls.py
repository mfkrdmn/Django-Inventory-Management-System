from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('staff', views.staff, name="dashboard-staff"),
    path('products', views.products, name="dashboard-products"),
    path('products/delete/<int:pk>/', views.product_delete, name="dashboard-product-delete"),
    path('products/edit/<int:pk>/', views.product_edit,name='dashboard-products-edit'),
    path('order', views.order, name="dashboard-order"),
]
