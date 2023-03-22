from rest_framework import serializers
from habits.models import Habit
from habits.validators import BonusValidator, TimeToCompleteValidator, EmptyBonusRelatedValidator,\
    RelatedHabitValidator, PleasantHabitValidator, FrequencyValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        exclude = ['user']
        validators = [
            BonusValidator(field=('related_habit', 'bonus')),
            TimeToCompleteValidator(field='time_to_complete'),
            EmptyBonusRelatedValidator(field=('pleasant_habit', 'related_habit', 'bonus')),
            RelatedHabitValidator(field='pleasant_habit'),
            PleasantHabitValidator(field=('pleasant_habit', 'related_habit', 'bonus')),
            FrequencyValidator(field='frequency')
        ]
