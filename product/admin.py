from django.contrib import admin
from .models import Product, CartItem, OrderItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["productname", "description" , "price", "stock","image","status"]


@admin.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    list_display = ["product", "quantity", "added_at"]

@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["product", "quantity", "ordered_at"]