from django.urls import path, include
from . import views
# from .views import login_page
urlpatterns = [
    path("", views.home, name="home"),
    path("cart/", views.cart, name="cart"),
    path("order/", views.order, name="order"),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('login/', login_page, name='login_page'),    # Login page
    # path('register/', register_page, name='register'),  # Registration page
]