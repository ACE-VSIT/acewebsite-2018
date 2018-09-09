from django.contrib import admin
from .models import ACEUserProfile, Tasks, Submissions
#from django_imgur.storage import ImgurStorage

admin.site.site_title = 'ACE - Selection Portal'
admin.site.site_header = 'ACE - Selection Portal'


@admin.register(ACEUserProfile)
class ACEUserAdmin(admin.ModelAdmin):
    # form = PhotoUnsignedDirectForm
    list_display = ('name', 'enroll_number', 'course', 'email_id', 'is_core', 'is_member', 'dateUpdated')
    search_fields = ['name__username', 'enroll_number', 'course']


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'task_id', 'difficulty_value', 'total_submissions')


@admin.register(Submissions)
class SubmissionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'submission_url', 'dateUpdated')
