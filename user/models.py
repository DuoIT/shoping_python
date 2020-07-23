from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=300, blank=True)
#     birth_date = models.DateField(null=True, blank=True)


class CustomerUser(AbstractUser):
    phone_number = models.CharField(default='', max_length=15)
    address = models.CharField(default='', max_length=255)


