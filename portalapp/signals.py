from django.db.models.signals import post_save, pre_delete

from django.dispatch import receiver
from django.contrib.auth.models import User

import cloudinary

from portalapp.models import ACEUserProfile
from scripts.sendgrid import send_sd_email

'''
Triggers a mail to join WhatsApp group!
'''

import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def join_wa_group(sender, instance, created, **kwargs):
    try:
        if created:
            subject = "Invitation for joining ACE WhatsApp Group"
            from_email = "vips.ace@gmail.com"
            to_email = instance.email
            name = str(instance.first_name)
            email_content = {
                'type': 'text/plain',
                'content': '''
Hey there!
We really appreciate your interest in ACE and would like to invite you to join our WhatsApp group.
If you have any questions, just leave a message here!
http://bit.ly/ACE-Selections-2018
            
Best,
Team ACE
'''
            }
            # send_sd_email(name, from_email, to_email, subject, email_content)

    except Exception as ex:
        pass


@receiver(pre_delete, sender=ACEUserProfile)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.picture.public_id)