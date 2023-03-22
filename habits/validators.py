from datetime import time
from rest_framework import serializers
from django.shortcuts import get_object_or_404

from habits.models import Habit


class BonusValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        related_habit = value.get('related_habit')
        bonus = value.get('bonus')
        pleasant_habit = value.get('pleasant_habit')

        if related_habit is not None and bonus is not None:
            raise serializers.ValidationError("Нельзя выбирать приятную привычку и вознаграждение одновременно")

        elif not pleasant_habit:
            if related_habit is None and bonus is None:
                raise serializers.ValidationError("Выберете приятную привычку или вознаграждение")


class TimeToCompleteValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time_to_complete = value.get('time_to_complete')

        if time_to_complete > time(minute=2):
            raise serializers.ValidationError("Время выполнения должно быть не более 2 минут")


class EmptyBonusRelatedValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if not value.get('pleasant_habit'):
            if (value.get('related_habit') is None) and (value.get('bonus') is None):
                raise serializers.ValidationError('Нельзя, чтобы связанная привычка и вознаграждение были одновременно пустые')


class RelatedHabitValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        related_habit = value.get('related_habit')

        if related_habit:
            tmp = get_object_or_404(Habit, pk=related_habit.pk)
            if not tmp.pleasant_habit:
                raise serializers.ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки")


class PleasantHabitValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        pleasant_habit = value.get('pleasant_habit')
        related_habit = value.get('related_habit')
        bonus = value.get('bonus')

        if pleasant_habit:
            if related_habit is not None or bonus is not None:
                raise serializers.ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки")


class FrequencyValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        frequency = value.get('frequency')

        if frequency:
            if frequency > 7:
                raise serializers.ValidationError("Периодичность не может быть более 7 дней")

