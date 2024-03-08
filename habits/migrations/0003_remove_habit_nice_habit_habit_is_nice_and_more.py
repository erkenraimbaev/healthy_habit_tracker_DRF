# Generated by Django 4.2.7 on 2024-03-06 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_alter_habit_nice_habit_alter_habit_period_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='nice_habit',
        ),
        migrations.AddField(
            model_name='habit',
            name='is_nice',
            field=models.BooleanField(default=False, verbose_name='признак приятной привычки'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='period',
            field=models.CharField(choices=[('two_times_a_week', 'два раза в неделю'), ('once_a_week', 'раз в неделю'), ('once_a_day', 'каждый день'), ('every_two_day', 'каждые два дня')], default='once_a_day', max_length=150, verbose_name='периодичность'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='related_habit',
            field=models.CharField(max_length=150, verbose_name='связанная  привычка'),
        ),
    ]