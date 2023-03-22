from django.conf import settings
from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):

    PUBLIC = 'public'
    PRIVATE = 'private'
    STATUSES = (
        ('public', 'публичная привычка'),
        ('private', 'приватная привычка')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='Место')
    time = models.TimeField(default='00:00', verbose_name='время исполнения')
    action = models.CharField(max_length=150, verbose_name='действие')
    pleasant_habit = models.BooleanField(default=False, verbose_name='приятная привычка')
    related_habit = models.ForeignKey("self", verbose_name='связанная привычка', on_delete=models.SET_NULL, **NULLABLE)
    frequency = models.IntegerField(default=1, verbose_name='периодичность выполнения привычки', **NULLABLE)
    bonus = models.CharField(max_length=200, verbose_name='вознаграждение', **NULLABLE)
    time_to_complete = models.TimeField(default='00:02', verbose_name='время на выполнение')
    status = models.CharField(max_length=20, choices=STATUSES, default=PUBLIC, verbose_name='признак публичности')

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'
