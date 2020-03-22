from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Customer(User):
    phone = models.CharField(max_length=20, unique=True)
    profile_pic = models.ImageField(default='default_av.png', upload_to='user_profile_pics')

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' - ' + self.phone

@receiver(post_save, sender=Customer)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)