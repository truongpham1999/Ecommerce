from django.db import models
from django.contrib.auth.models import User

from store.models import Product

# Create your models here.

class ShippingAddress(models.Model):
    # Authenticated / unauthenticated user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shipping_address', null=True, blank=True)

    full_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    
    address1 = models.CharField(max_length=400)
    address2 = models.CharField(max_length=400)

    city = models.CharField(max_length=250)
    district = models.CharField(max_length=250)
    ward = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Shipping Addresses'

    def __str__(self):
        return f"{self.full_name} - {self.phone_number} - {self.email}"
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)

    full_name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    shipping_address = models.TextField(max_length=1000)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.amount_paid} - {self.date}"
    

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_items', null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items', null=True)

    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return f"{self.user} - {self.product} - {self.quantity}"