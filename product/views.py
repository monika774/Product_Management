from django.shortcuts import render, redirect
from .models import Product, CartItem
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json
# from django.contrib import messages
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from .models import *

def home(request):
    """list of product items"""
    product = Product.objects.all()
    return render(request, "home.html", {"product": product})

def add_to_cart(request):
    """"Add item to cart"""
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        productname = request.POST.get('productname')
        status = request.POST.get('status')
        print("hello",product_id, productname)
        quantity = request.POST.get('quantity', 1)
        print("hii",quantity)
        try:
            product = Product.objects.get(id=product_id)
            if product.status != 'valid':
                return JsonResponse({'status': 'error', 'message': 'This product cannot be added to the cart as it is invalid.'})
            print(product)
            cart_item, created = CartItem.objects.get_or_create(product=product)
            cart_item.quantity = int(quantity)
            print(cart_item.quantity)
            cart_item.save()
            message = 'Product added to cart successfully!' 
            return JsonResponse({'status': 'success', 'message': message})
        except Product.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Product does not exist.'})
    return redirect('home')

def cart(request):
    """list of cart items"""
    cart_items = CartItem.objects.all()
    return render(request, "cart.html", {"cart_items": cart_items})

def order(request):
    """list of order items"""
    cart_items = CartItem.objects.all()
    return render(request, "order.html")

# def remove_from_cart(request, item_id):
#     """remove of item from cart list"""
#     try:
#         cart_item = CartItem.objects.get(id=item_id)
#         cart_item.delete()
#         return JsonResponse({'status': 'success', 'message': 'Product removed from cart successfully!'})
#     except CartItem.DoesNotExist:
#         return JsonResponse({'status': 'error', 'message': 'Product does not exist in the cart.'})
#     return redirect('cart')

def remove_from_cart(request, item_id):
    """Update quantity or remove item from cart"""
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id)
        try:
            quantity = int(request.POST.get('quantity', cart_item.quantity)) 
            print(quantity)
            if quantity > 0:
                cart_item.quantity = quantity  
                cart_item.save()
                return JsonResponse({ 'status': 'success','message': 'Quantity updated successfully!','new_quantity': cart_item.quantity
                })
            else:
                cart_item.delete()
                return JsonResponse({ 'status': 'success', 'message': 'Product removed from cart successfully!', 'new_quantity': 0
                })

        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Invalid quantity value.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

