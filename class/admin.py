from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Class)
admin.site.register(models.Routine)
admin.site.register(models.Teacher)
# admin.site.register(models.Resources)