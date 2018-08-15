from django.contrib import admin
from .models import ACEUserProfile, Tasks, Submissions

admin.site.site_title = 'ACE - RECRUITMENT PORTAL'
admin.site.site_header = 'ACE - RECRUITMENT PORTAL'


class ACEUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'enroll_number', 'course', 'email_id', 'is_core', 'is_member')
    search_fields = ['name__username', 'enroll_number', 'course']


class TasksAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'task_id', 'difficulty_value', 'submission_deadline')


class SubmissionsAdmin(admin.ModelAdmin):
    # list_display = ('task_name', 'task_id', 'difficulty_value', 'submission_deadline')
	pass


admin.site.register(ACEUserProfile, ACEUserAdmin)
admin.site.register(Tasks, TasksAdmin)
admin.site.register(Submissions, SubmissionsAdmin)
