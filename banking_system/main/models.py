from django.db import models
from django.contrib.auth.models import AbstractUser

class Branch(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    branch_name = models.CharField(max_length=255)
    def __str__(self):
        return self.branch_name

class Customer(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    id = models.AutoField(primary_key=True, unique=True)
    Customer_name = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE, default=1)  # Ensure default branch exists
    phone_number = models.CharField(max_length=15, unique=True)
    email_customer = models.CharField(max_length=255, null=True, default=None)
    def __str__(self):
        return self.Customer_name
