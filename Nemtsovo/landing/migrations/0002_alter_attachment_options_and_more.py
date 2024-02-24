# Generated by Django 5.0.1 on 2024-02-05 21:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachment',
            options={'verbose_name': 'Фото/Видео', 'verbose_name_plural': 'Фото/Видео'},
        ),
        migrations.AlterModelOptions(
            name='bookingconditions',
            options={'verbose_name': 'Условия бронирования', 'verbose_name_plural': 'Условия бронирования'},
        ),
        migrations.AlterModelOptions(
            name='period',
            options={'verbose_name': 'Период', 'verbose_name_plural': 'Периоды'},
        ),
        migrations.AddField(
            model_name='house',
            name='duration',
            field=models.PositiveIntegerField(default=1, verbose_name='Продолжительность'),
        ),
        migrations.AlterField(
            model_name='house',
            name='booking_conditions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='landing.bookingconditions', verbose_name='Условия бронирования'),
        ),
    ]