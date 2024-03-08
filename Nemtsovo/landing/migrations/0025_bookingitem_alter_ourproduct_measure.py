# Generated by Django 5.0.1 on 2024-02-25 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0024_remove_ourproduct_order_alter_ourproduct_measure'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Идентификатор бронируемого объекта',
                'verbose_name_plural': 'Индентификаторы бронируемых объектов',
            },
        ),
        migrations.AlterField(
            model_name='ourproduct',
            name='measure',
            field=models.CharField(choices=[('л', 'литр'), ('шт', 'штука'), ('г', 'грамм'), ('кг', 'килограмм')], default=('шт', 'штука'), max_length=4, verbose_name='Ед. измерения'),
        ),
    ]