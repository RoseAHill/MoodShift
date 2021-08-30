from time import strftime
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Entry
from .forms import EntryForm
import html
import calendar
from calendar import HTMLCalendar, month
from datetime import date
from .moods import moods, moodChoices

class Home(LoginView):
  template_name = 'home.html'

today = date.today()

# Create your views here.

class EntryCreate(LoginRequiredMixin, CreateView):
  model = Entry
  fields = ['entryDate', 'description', 'mood']
  success_url = '/journal/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  

class EntryDelete(LoginRequiredMixin, DeleteView):
  model = Entry
  success_url = f'/journal/{today.year}/{today.month}/'

@login_required
def entryHome(request):
  entry_form = EntryForm()
  print(entry_form)
  return render(request, 'entryHome.html', {
    'entry_form': entry_form,
  })

def about(request):
  return render(request, 'about.html', {
    'this_month': today.month,
    'this_year': today.year,
  })

@login_required
def journal(request, year, month):
  year = int(year)
  month = int(month)

  cal = HTMLCalendar(firstweekday=6).formatmonth(year, month)

  # Get the entries within that month & store them into an array
  entries_this_month = Entry.objects.filter(entryDate__year=year, entryDate__month=month)
  for day_num in range(1, calendar.monthrange(int(year), month)[1] + 1):
    for entry in entries_this_month:
      if entry.entryDate.day == day_num:
        mood_dict = moods.get(entry.mood)
        cal = cal.replace(f"\">{str(day_num)}<", f" {entry.mood}\"><button class='moodshift-emoji' type='button' data-bs-toggle='offcanvas' data-bs-target='#offcanvas{str(day_num)}' aria-controls='offcanvas{str(day_num)}'><i class='far fa-{mood_dict.get('faicon')}'></i></button><")
    
  return render(request, 'journal.html', {
    "entries": entries_this_month,
    "year": year,
    "month": month,
    "month_name": strftime('%B'),
    "cal": cal,
  })

def journalHome(request):
  return redirect('journal', year=2021, month=8)

def signup(request):
  error_message = ""
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = "Invalid signup - try again"
  form = UserCreationForm()
  context = {"form": form, "error_message": error_message}
  return render(request, 'userauth.html', context)