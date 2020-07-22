from django.db import models
from product.models import Validation
from user.models import CustomerUser
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Validation, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
