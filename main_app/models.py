from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class Mood(models.Model):
  alias = models.CharField
  reaction = models.CharField
  faicon = models.CharField

class Entry(models.Model):
  entryDate = models.DateField
  description = models.TextField(max_length=1000)
  mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)