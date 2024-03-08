# Generated by Django 5.0.1 on 2024-03-06 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0033_alter_ourproduct_measure_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date_end_fact',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Фактическое окончание бронирования'),
        ),
        migrations.AddField(
            model_name='booking',
            name='date_start_fact',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Фактическое начало бронирования'),
        ),
        migrations.AlterField(
            model_name='ourproduct',
            name='measure',
            field=models.CharField(choices=[('л', 'литр'), ('г', 'грамм'), ('шт', 'штука'), ('кг', 'килограмм')], default=('шт', 'штука'), max_length=4, verbose_name='Ед. измерения'),
        ),
    ]
