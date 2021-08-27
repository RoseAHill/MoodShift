from django.db import models

# Create your models here.

class Entry(models.Model):
  date = models.DateField
  description = models.TextField(max_length=1000)