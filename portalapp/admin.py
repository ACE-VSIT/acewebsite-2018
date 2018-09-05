from django.contrib import admin
from .models import ACEUserProfile, Tasks, Submissions

admin.site.site_title = 'ACE - Selection Portal'
admin.site.site_header = 'ACE - Selection Portal'


class ACEUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'enroll_number', 'course', 'email_id', 'is_core', 'is_member', 'dateUpdated')
    search_fields = ['name__username', 'enroll_number', 'course']


class TasksAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'task_id', 'difficulty_value', 'total_submissions')


class SubmissionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'submission_url', 'dateUpdated')


admin.site.register(ACEUserProfile, ACEUserAdmin)
admin.site.register(Tasks, TasksAdmin)
admin.site.register(Submissions, SubmissionsAdmin)
