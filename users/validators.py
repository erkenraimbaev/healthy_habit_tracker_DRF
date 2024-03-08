from rest_framework import serializers


class TelegramIdValidator:
    def __init__(self, telegram_id) -> None:
        self.telegram_id = telegram_id

    def __call__(self, value):
        ids_tel = value.get(self.telegram_id)
        if len(ids_tel) != 10:
            raise serializers.ValidationError("Неверное значение id telegram!")