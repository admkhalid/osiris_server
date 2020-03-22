from django.db import models
from django.contrib.auth.models import AbstractUser
from market.models import Hub

class User(AbstractUser):
    is_merch = models.BooleanField()
    profile_pic = models.ImageField(default='default_av.png', upload_to='merch_profile_pics')
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' - ' + self.phone

class MerchProfile(User):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
