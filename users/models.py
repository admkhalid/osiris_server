from django.db import models
from django.contrib.auth.models import User
from market.models import Hub

class MerchProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    is_merch = models.BooleanField(default=True)
    profile_pic = models.ImageField(default='default_av.png', upload_to='merch_profile_pics')
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)

    class Meta:
        db_table = 'merch_profile'

class CustProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    is_merch = models.BooleanField(default=False)
    profile_pic = models.ImageField(default='default_av.png', upload_to='merch_profile_pics')