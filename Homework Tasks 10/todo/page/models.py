from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(blank=False)
    priority = models.IntegerField()
    created_at = models.DateTimeField(blank=True)
# Create your models here.
