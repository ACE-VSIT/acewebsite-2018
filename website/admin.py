from django.contrib import admin
from .models import *


@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'enrollment_number', 'position', 'email',)
    pass
@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name','desc','created_by','tools',)
    pass
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name','desc','ev_date',)
    pass
@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ('team','ev_name','college_name',)
    pass
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('imag','desc',)
    pass
@admin.register(UpEvent)
class UpEventAdmin(admin.ModelAdmin):
    list_display = ('name','desc','ev_date','registration_url',)
    pass
@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ('name','ev_date',)
    pass