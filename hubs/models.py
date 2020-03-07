from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hub(models.Model):
    hub_id = models.CharField(max_length=25, primary_key=True)
    x_co_ord = models.DecimalField(max_digits=9, decimal_places=6)
    y_co_ord = models.DecimalField(max_digits=9, decimal_places=6)
    area = models.CharField(max_length=50)
    area_code = models.IntegerField() 

    def __str__(self):
        return self.area + ' ' + self.hub_id

class Merchant(User):
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' - ' + self.phone

class Product(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete = models.CASCADE, related_name='products')
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    avail_quantity = models.FloatField()