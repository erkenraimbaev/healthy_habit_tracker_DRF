from datetime import datetime

from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """
    Модель для создания ваших полезных привычек
    """

    PERIODS = {
        ('once_a_day', 'каждый день'),
        ('every_two_day', 'каждые два дня'),
        ('two_times_a_week', 'два раза в неделю'),
        ('once_a_week', 'раз в неделю'),

    }
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='')
    place = models.CharField(max_length=150, default='в любом месте', verbose_name='место')
    time_habit = models.TimeField(verbose_name='время', default=datetime.now().time())
    action = models.CharField(max_length=150, verbose_name='действие')
    is_nice = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная  привычка', **NULLABLE)
    period = models.CharField(max_length=150, choices=PERIODS, default='once_a_day', verbose_name='периодичность')
    reward = models.CharField(max_length=200, verbose_name='вознаграждение', **NULLABLE)
    seconds_to_complete = models.PositiveIntegerField(verbose_name='время на выполнение в секундах')
    is_public = models.BooleanField(default=False, verbose_name='признак публичной привычки')

    def __str__(self):
        return f'Я буду {self.action} {self.place} в {self.time_habit}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
