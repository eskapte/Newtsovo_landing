# Generated by Django 5.0.1 on 2024-03-16 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0039_booking_is_dayly_alter_booking_date_end_fact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_late_checkout',
            field=models.BooleanField(default=False, verbose_name='Поздний выезд'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date_end_fact',
            field=models.DateTimeField(blank=True, help_text='Если это посуточное бронирование, то указывайте здесь, пожалуйста, последний полный день, чтобы система бронирования следующий день помечала как свободный', null=True, verbose_name='Дата окончания бронирования'),
        ),
        migrations.AlterField(
            model_name='ourproduct',
            name='measure',
            field=models.CharField(choices=[('шт', 'штука'), ('кг', 'килограмм'), ('г', 'грамм'), ('л', 'литр')], default=('шт', 'штука'), max_length=4, verbose_name='Ед. измерения'),
        ),
    ]
