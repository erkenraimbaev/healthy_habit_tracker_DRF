from django.urls import path
from rest_framework import routers

from habits.views import HabitListView, HabitDetailView, HabitCreateView, \
    HabitUpdateView, HabitDeleteView, PublicHabitListView

from habits.apps import HabitsConfig

app_name = HabitsConfig.name

urlpatterns = [
                  path('habits/', HabitListView.as_view(), name='habit-list'),
                  path('habits_public/', PublicHabitListView.as_view(), name='habit-public-list'),
                  path('habits/<int:pk>/', HabitDetailView.as_view(), name='habit'),
                  path('habits/create/', HabitCreateView.as_view(), name='habit-create'),
                  path('habits/update/<int:pk>/', HabitUpdateView.as_view(), name='habit-update'),
                  path('habits/delete/<int:pk>/', HabitDeleteView.as_view(), name='habit-delete'),
              ]
