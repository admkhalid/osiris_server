from django.db import models
from django.contrib.auth.models import User

class Hub(models.Model):
    hub_id = models.CharField(max_length=25, primary_key=True)
    x_co_ord = models.DecimalField(max_digits=9, decimal_places=6)
    y_co_ord = models.DecimalField(max_digits=9, decimal_places=6)
    area = models.CharField(max_length=50)
    area_code = models.IntegerField() 

    def __str__(self):
        return self.area + ' ' + self.hub_id

class Product(models.Model):
    merchant = models.ForeignKey(User, on_delete = models.CASCADE, related_name='products')
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    image = models.ImageField(default='default_item.jpg', upload_to='prod_pics')
    avail_quantity = models.DecimalField(max_digits=10, decimal_places=3)
    rate = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.name + ' ' + self.family + ' - ' + str(self.avail_quantity) + ' from ' + self.merchant.__str__()