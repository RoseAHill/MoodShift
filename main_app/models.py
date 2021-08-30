from django.db import models
from datetime import date
from django.contrib.auth.models import User
from .moods import moodChoices

class Entry(models.Model):
  entryDate = models.DateField(
    default=date(2021, 1, 1)
  )
  description = models.TextField(max_length=1000)
  mood = models.CharField(
    max_length=20,
    choices=moodChoices,
    default=moodChoices[3][0]
  )
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.entryDate.strftime('%d/%m/%Y')} - {self.description}"
  
