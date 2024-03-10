from rest_framework import serializers

from habits.models import Habit
from habits.validators import RewardOrNiceHabitValidator, HabitTime120Validator, RelatedHabitIsNiceValidator, \
    NiceHabitNoRewardValidator, PeriodValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'


class HabitCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'id', 'user', 'place', 'time_habit', 'action', 'is_nice', 'related_habit', 'period', 'seconds_to_complete',
            'reward',)
        validators = [
            RewardOrNiceHabitValidator(fields),
            HabitTime120Validator(field='seconds_to_complete'),
            PeriodValidator(field='period'),
            RelatedHabitIsNiceValidator(fields),
            NiceHabitNoRewardValidator(fields)
        ]
