from django.db import models

class TaskModel(models.Model):
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Tasks"
