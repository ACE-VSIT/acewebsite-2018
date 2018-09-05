from django.contrib import admin

from admin_email_sender.models import SendEmail_User, SendEmail_ACEUserProfile
from portalapp.models import ACEUserProfile


@admin.register(SendEmail_User)
class SendEmail_UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('users',)

    list_display = ('subject', 'created_at', 'total_emails', 'status',)

    def total_emails(self, obj):
        return obj.users.count()


@admin.register(SendEmail_ACEUserProfile)
class SendEmail_ACEUserProfileMemberAdmin(admin.ModelAdmin):
    # filter_horizontal = ('members',)

    list_display = ('subject', 'created_at', 'total_emails', 'status',)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "members":
            kwargs["queryset"] = ACEUserProfile.objects.filter(is_member=True)
        return super(SendEmail_ACEUserProfileMemberAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    def total_emails(self, obj):
        return obj.members.count()


# Need to create a proxy as we can't register two models in Admin
class SendEmail_ACEUserProfileCore(SendEmail_ACEUserProfile):
    class Meta:
        proxy = True
        verbose_name = 'Email ACE Core Member'


@admin.register(SendEmail_ACEUserProfileCore)
class SendEmail_ACEUserProfileCoreMemberAdmin(admin.ModelAdmin):
    filter_horizontal = ('members',)

    list_display = ('subject', 'created_at', 'total_emails', 'status',)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "members":
            kwargs["queryset"] = ACEUserProfile.objects.filter(is_core=True)
        return super(SendEmail_ACEUserProfileCoreMemberAdmin, self).formfield_for_manytomany(db_field, request,
                                                                                             **kwargs)

    def total_emails(self, obj):
        return obj.members.count()

