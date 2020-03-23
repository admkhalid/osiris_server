from django.contrib.auth.models import User
from .models import MerchProfile
from django.db.models.signals import post_save
from django.dispatch import receiver

# @receiver(post_save, sender=User)
# def create_merch_profile(sender, instance=None, created=False, **kwargs):
#     if created:
#         MerchProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_merch_profile(sender, instance=None, **kwargs):
#     if instance.is_merch:
#         instance.profile.save()