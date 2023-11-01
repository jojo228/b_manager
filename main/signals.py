from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Entrepreneur
from .models import User


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Entrepreneur.objects.create(user=instance)
    instance.staff.save()
