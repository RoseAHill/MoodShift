from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('journal/<int:year>/<str:month>/', views.journal, name='journal'),
  path('journal/', views.journalHome, name='journal_home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('journal/create/', views.EntryCreate.as_view(), name='entry_create')
]