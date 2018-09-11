from django.contrib import admin

from library.models import Assignment, Resources, Categories, Attendance


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Resources)
class ResourceAdmin(admin.ModelAdmin):
    # list_display = ('Category', 'Course', 'Author', 'URL', 'approval_status')
    pass
