from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other customer fields (e.g., name, email, address)

class Call(models.Model):
    call_type = models.CharField(max_length=100, default="Physical")
    call_category = models.CharField(max_length=100, default="Sale")

class Channel(models.Model):
    channel_type = models.CharField(max_length=100, default="Physical Visit")

class Representative(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.CharField(max_length=100, default=None)
    payment_code = models.CharField(max_length=100, null=True, blank=True)
    cheque_date = models.DateTimeField(null=True, blank=True)

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    call = models.ForeignKey(Call, on_delete=models.CASCADE, default="Physical")
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, default="Physical Visit")
    representative = models.ForeignKey(Representative, on_delete=models.CASCADE, default="None")
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(default="2023-06-06")
    region = models.CharField(max_length=100, default="Nairobi")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(default="No Comment")

    def __str__(self):
        return f"{self.customer.user.username} - {self.date}"
