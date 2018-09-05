from django.contrib.auth.models import User
from django.db import models

from admin_email_sender.helpers import *

from portalapp.models import ACEUserProfile


class SendEmail_User(models.Model):
    subject = models.CharField(max_length=100, null=False, blank=False)
    text = models.TextField(null=False, blank=False, help_text=BODY_HELPER)
    users = models.ManyToManyField(User, blank=False, related_name='+')
    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True
    )

    class Meta:
        verbose_name = 'Email all User'


class SendEmail_ACEUserProfile(models.Model):
    subject = models.CharField(max_length=100, null=False, blank=False)
    text = models.TextField(null=False, blank=False, help_text=BODY_HELPER)
    members = models.ManyToManyField(ACEUserProfile, blank=False, related_name='+')
    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True
    )

    class Meta:
        verbose_name = 'Email ACE Member'

