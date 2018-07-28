from django.contrib import admin
from .models import Members


@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'email',)
    pass
