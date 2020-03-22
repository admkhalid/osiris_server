from django.conf import settings
from .models import MerchProfile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created and instance.is_merch:
        MerchProfile.objects.create(user=instance)