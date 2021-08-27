from django.shortcuts import render
from django.http import HttpResponse
import calendar
from calendar import HTMLCalendar, month
from datetime import date

class Entry:
  def __init__(self, entry_date, mood, description):
    self.date = entry_date
    self.mood = mood
    self.description = description

entries = [
  Entry(date(2021, 8, 20), "good", "I had a good day")
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>How are you feeling today?</h1>')

def about(request):
  return render(request, 'about.html')

def journal(request, year, month):
  month = month.capitalize()
  month_number = int(list(calendar.month_name).index(month))

  cal = HTMLCalendar().formatmonth(year, month_number)

  return render(request, 'journal.html', {
    "entries": [],
    "selected_entry": {},
    "year": year,
    "month": month,
    "month_number": month_number,
    "cal": cal,
  })