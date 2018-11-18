from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


PAYMENT = (
    ('cash','CASH'),
    ('credit_card','CREDIT CARD')
)

STATUS = (
    ('pending','PENDING'),
    ('paid','PAID')
)

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    phone_number = PhoneNumberField(null=True)
    payment_type = models.CharField(max_length=10, choices=PAYMENT, default='cash')
    status = models.CharField(max_length=10, choices=STATUS, default='pending')
    created = models.DateTimeField(auto_now_add=True)
