# Generated by Django 4.2.7 on 2024-03-06 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='nice_habit',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='приятная привычка'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='period',
            field=models.CharField(choices=[('once_a_week', 'раз в неделю'), ('two_times_a_week', 'два раза в неделю'), ('every_two_day', 'каждые два дня'), ('once_a_day', 'каждый день')], default='once_a_day', max_length=150, verbose_name='периодичность'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='reward',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='вознаграждение'),
        ),
    ]