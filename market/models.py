from django.db import models

# Create your models here.

class Hub(models.Model):
    hub_id = models.CharField(max_length=25, primary_key=True)
    x_co_ord = models.DecimalField(max_digits=9, decimal_places=6)
    y_co_ord = models.DecimalField(max_digits=9, decimal_places=6)
    area = models.CharField(max_length=50)
    area_code = models.IntegerField() 

    def __str__(self):
        return self.area + ' ' + self.hub_id