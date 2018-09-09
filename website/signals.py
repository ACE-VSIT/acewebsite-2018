import cloudinary
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from website.models import Image, Project


@receiver(pre_delete, sender=Project)
@receiver(pre_delete, sender=Image)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.picture.public_id)
