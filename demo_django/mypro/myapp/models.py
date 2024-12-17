from django.db import models

class TodoItem(models.Model):
    title1 = models.CharField(max_length=100)
