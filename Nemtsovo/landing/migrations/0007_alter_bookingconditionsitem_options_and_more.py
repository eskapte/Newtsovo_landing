# Generated by Django 5.0.1 on 2024-02-07 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0006_remove_bookingconditions_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookingconditionsitem',
            options={'verbose_name': 'Пункт в условиях', 'verbose_name_plural': 'Пункты в условиях'},
        ),
        migrations.RemoveField(
            model_name='bookingconditions',
            name='name',
        ),
        migrations.AddField(
            model_name='bookingconditions',
            name='displayed_name',
            field=models.CharField(default='Условия бронирования', help_text='Название, которое будет отображаться на сайте', max_length=100, verbose_name='Отображаемое название'),
        ),
        migrations.AddField(
            model_name='bookingconditions',
            name='inner_name',
            field=models.CharField(default='Условия бронирования', help_text='Это название уже для вашего удобства, оно отображается здесь, в админке', max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='bookingconditionsitem',
            name='text',
            field=models.CharField(max_length=500, verbose_name='Текст пункта'),
        ),
    ]
