from ace import settings
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from admin_email_sender.models import SendEmail_User, SendEmail_ACEUserProfile
from admin_email_sender.utils import EmailThread, replace_text


@receiver(m2m_changed, sender=SendEmail_User.users.through)
def send_email_signal(sender, instance, **kwargs):
    users = instance.users.all()
    text = instance.text
    html_text = text.replace('\n', '<br>')
    if users:
        for user in users:
            EmailThread(subject=instance.subject,
                        message=replace_text(text, user),
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[user.email],
                        fail_silently=True,
                        html_message=replace_text(html_text, user)).start()
            print(user.email)
        instance.status = True

    instance.save()


@receiver(m2m_changed, sender=SendEmail_ACEUserProfile.members.through)
def send_email_signal(sender, instance, **kwargs):
    users = instance.members.all()
    text = instance.text
    html_text = text.replace('\n', '<br>')
    if users:
        for user in users:
            EmailThread(subject=instance.subject,
                        message=replace_text(text, user.name),
                        from_email=settings.EMAIL_DEFAULT_SENDER,
                        recipient_list=[user.email_id],
                        fail_silently=False,
                        html_message=replace_text(html_text, user.name)).start()
            print(user.email_id)
        instance.status = True

    instance.save()
