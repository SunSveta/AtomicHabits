from datetime import timedelta, datetime
from celery import shared_task
from django.conf import settings
import requests
from habits.models import Habit
from rest_framework.response import Response


def send_message(text):
    data_for_request = {
        "chat_id": f"{settings.TELEGRAM_CHAT_ID}", #TODO wtf chat_id? (Found wideo)
        "text": text
    }
    response = requests.get(f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage',  #sendMe or sendMessage
                            data_for_request)
    return Response(response.json())


@shared_task
def check_time():  #TODO check work of thi task

    time = datetime.now().time()
    start_time = datetime.now() - timedelta(minutes=1)
    habits_lst = Habit.objects.filter(time__gte=start_time)
    for habit in habits_lst.filter(time__lte=time):
        text = f'Я буду {habit.action} в {habit.time} в {habit.place}'
        send_message(text)
