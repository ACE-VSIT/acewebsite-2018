from django.contrib import admin
from .models import *


@admin.register(Member)
class MembersAdmin(admin.ModelAdmin):
    # list_display = ('name', 'enrollment_number', 'position', 'email',)
    pass


@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    # list_display = ('name', 'desc', 'created_by', 'tools',)
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # list_display = ('name', 'desc', 'ev_date',)
    pass


@admin.register(Achievement)
class AchievementsAdmin(admin.ModelAdmin):
    # list_display = ('team', 'ev_name', 'college_name',)
    pass


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    # list_display = ('image', 'desc',)
    pass


@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    # list_display = ('name', 'ev_date',)
    pass
