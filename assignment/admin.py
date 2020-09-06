from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Roles', {'fields': ('is_teacher','is_student','is_admin')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Roles', {'fields': ('is_teacher','is_student','is_admin')}),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Student)
# admin.site.register(Subject)
admin.site.register(Assignment)
admin.site.register(StudentAnswer)


