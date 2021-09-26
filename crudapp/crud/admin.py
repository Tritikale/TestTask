from django.contrib import admin
from .models import Task


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'description')
    list_editable = ('title', 'description')


admin.site.register(Task, TaskAdmin)
