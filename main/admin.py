from django.contrib import admin
from main.models import TaskModel

class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "is_done", "created_at", "updated_at"]
    search_fields = ["title"]

admin.site.register(TaskModel, TaskAdmin)
