# Generated by Django 4.2.7 on 2024-03-08 07:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0006_alter_habit_period_alter_habit_time_habit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='period',
            field=models.CharField(choices=[('once_a_week', 'раз в неделю'), ('two_times_a_week', 'два раза в неделю'), ('once_a_day', 'каждый день'), ('every_two_day', 'каждые два дня')], default='once_a_day', max_length=150, verbose_name='периодичность'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='time_habit',
            field=models.TimeField(default=datetime.time(12, 31, 15, 800739), verbose_name='время'),
        ),
    ]