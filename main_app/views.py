from django.shortcuts import render
import html
from django.http import HttpResponse
import calendar
from calendar import HTMLCalendar, month
from datetime import date

class Mood:
  def __init__(self, alias, reaction, faicon):
    self.alias = alias
    self.reaction = reaction
    self.faicon = faicon

moods = [
  Mood("fantastic", "Yay! That's so awesome!", "laugh-beam"),
  Mood("great", "That's great to hear!", "smile-beam"),
  Mood("good", "I'm glad you're doing well.", "smile"),
  Mood("neutral", "That's better than not okay, so I'm glad!", "meh"),
  Mood("down", "That's understandable, we all have those days.", "frown"),
  Mood("annoyed", "That can be a frustrating feeling.", "angry"),
  Mood("overwhelmed", "Take one step at a time and take deep breaths. Everything is going to be okay.", "tired"),
]

class Entry:
  def __init__(self, entry_date, mood, description):
    self.date = entry_date
    self.mood = mood
    self.description = html.escape(description)

entries = [
  Entry(date(2021, 8, 20), moods[1], "I had a good day. Good things happened."),
  Entry(date(2021, 8, 13), moods[5], "Annoying things happened"),
  Entry(date(2021, 7, 10), moods[2], "Many good things"),
  Entry(date(2021, 7, 4), moods[0], "I had a lot of awesome things happen"),
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def journal(request, year, month):
  month = month.capitalize()
  month_number = int(list(calendar.month_name).index(month))
  cal = HTMLCalendar(firstweekday=6).formatmonth(year, month_number)
  
  # Get the entries within that month & store them into an array
  entries_this_month = []
  days_with_entries = []
  for entry in entries:
    if entry.date.year == year and entry.date.month == month_number:
      entries_this_month.append(entry)
      days_with_entries.append(int(entry.date.day))
  for day_num in range(1, calendar.monthrange(int(year), month_number)[1] + 1):
    if (day_num in days_with_entries):
      for entry in entries_this_month:
        if entry.date.day == day_num:
          cal = cal.replace(f"\">{str(day_num)}<", f" {entry.mood.alias}\"><button class='moodshift-emoji' type='button' data-bs-toggle='offcanvas' data-bs-target='#offcanvas{day_num}' aria-controls='offcanvas{day_num}'><i class='far fa-{entry.mood.faicon}'></i></button><")

      
  return render(request, 'journal.html', {
    "entries": entries_this_month,
    "selected_entry": {},
    "year": year,
    "month": month,
    "month_number": month_number,
    "cal": cal,
  })