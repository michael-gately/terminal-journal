from django.db import models

# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=50)
    caption = models.CharField(max_length=500)
    created_date = models.DateField()