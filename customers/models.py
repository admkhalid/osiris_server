from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from hubs.models import Product

class Customer(User):
    phone = models.CharField(max_length=20, unique=True)
    profile_pic = models.ImageField(default='default_av.png', upload_to='user_profile_pics')
    address = models.TextField(default='')

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' - ' + self.phone

class CartItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    ordered = models.BooleanField(default=False)
    processed = models.BooleanField(default=False)

class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    processed = models.BooleanField(default=False)

@receiver(post_save, sender=Customer)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)