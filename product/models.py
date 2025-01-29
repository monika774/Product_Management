from django.db import models
from django.contrib.auth.models import User
# 
# Model of product
class Product(models.Model):
    STATUS_CHOICES = [
        ('valid', 'Valid'),
        ('invalid', 'Invalid'),
    ]
    productname = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=150, blank=False)
    price = models.FloatField(null=False)  
    stock = models.IntegerField()
    image = models.CharField(max_length=200, null=False)
    status = models.CharField(
        max_length=7,
        choices=STATUS_CHOICES,
        default='valid',
    )
    # def save(self, *args, **kwargs):
    #     # Automatically set status to 'invalid' if stock is less than 0
    #     if self.stock < 0:
    #         self.status = 'invalid'
    #     else:
    #         self.status = 'valid'
        # super().save(*args, **kwargs)
    def __str__(self):
        return self.productname


# Model of CartItem
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    quantity = models.IntegerField(default=1)  
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.productname}"


# Model of OrderItem
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    quantity = models.IntegerField(default=1)  
    ordered_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return self.product.price * self.quantity
       

       