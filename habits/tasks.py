from django.conf import settings
from celery import shared_task
import requests

from habits.models import Habit


@shared_task
def good_habit_sender():
    TOKEN = settings.TELEGRAM_BOT_TOKEN
    SEND_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    habits = Habit.objects.all()

    for hab in habits:
        'я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]'
        text = f'В {hab.time_habit} я буду {hab.action} в {hab.place}.\n' + \
               'Наградой будет:'
        if hab.reward:
            text += f' {hab.reward}.'
        text += f'Выполнять нужно {hab.period}'

        response = requests.post(SEND_URL, json={'chat_id': hab.user.telegram_id, 'text': text})
