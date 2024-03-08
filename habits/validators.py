from rest_framework import serializers


class RewardOrNiceHabitValidator:
    """
    Проверка что нельзя одновременно выбрать связанную привычку и награду
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        related_habit = dict(value).get('related_habit')
        reward = dict(value).get('reward')

        if reward and related_habit:
            raise serializers.ValidationError("Нельзя одновременно выбрать связанную привычку и награду.")


class HabitTime120Validator:
    """
    Проверка на выполнение по времени (не больше 120 секунд)
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time_habit = dict(value).get(self.field)
        if time_habit > 120:
            raise serializers.ValidationError("Время выполнения должно быть не больше 120 секунд.")


class RelatedHabitIsNiceValidator:
    """
    Проверка на признак приятной привычки
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        related_habit = dict(value).get('related_habit')
        if related_habit:
            if not related_habit.is_nice:
                raise serializers.ValidationError("Связанная привычка должна быть приятной.")


class NiceHabitNoRewardValidator:
    """
    Проверка параметров приятной привычки
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        is_nice = dict(value).get('is_nice')
        related_habit = dict(value).get('related_habit')
        reward = dict(value).get('reward')
        if is_nice and related_habit or reward:
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки.")
