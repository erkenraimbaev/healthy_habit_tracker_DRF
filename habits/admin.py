from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('action', 'period', 'is_nice', 'related_habit', 'reward', 'seconds_to_complete', 'is_public')
    list_filter = ('is_public', 'is_public',)
    search_fields = ('user',)
