# Generated by Django 4.2.7 on 2024-03-08 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0007_alter_habit_period_alter_habit_time_habit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='period',
            field=models.CharField(choices=[('once_a_week', 'раз в неделю'), ('every_two_day', 'каждые два дня'), ('once_a_day', 'каждый день'), ('two_times_a_week', 'два раза в неделю')], default='once_a_day', max_length=150, verbose_name='периодичность'),
        ),
        migrations.RemoveField(
            model_name='habit',
            name='place',
        ),
        migrations.AlterField(
            model_name='habit',
            name='time_habit',
            field=models.TimeField(default=datetime.time(12, 52, 46, 327121), verbose_name='время'),
        ),
        migrations.DeleteModel(
            name='HabitPlace',
        ),
        migrations.AddField(
            model_name='habit',
            name='place',
            field=models.CharField(default='в любом месте', max_length=150, verbose_name='место'),
        ),
    ]
