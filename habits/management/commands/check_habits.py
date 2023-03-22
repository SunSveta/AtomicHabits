import json
from datetime import datetime, timedelta
import pytz
from django.conf import settings
from django.core.management import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class Command(BaseCommand):

    def handle(self, *args, **options):
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=60,
            period=IntervalSchedule.SECONDS,
        )

        PeriodicTask.objects.create(
            interval=schedule,  # we created this above.
            name='Check habit time',  # simply describes this periodic task.
            task='habits.tasks.check_time',  # name of task.

            expires=datetime.now().astimezone(pytz.timezone(settings.TIME_ZONE)) + timedelta(days=365)
        )