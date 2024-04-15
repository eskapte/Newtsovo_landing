# Generated by Django 5.0.1 on 2024-04-14 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0050_errorlog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='errorlog',
            options={'ordering': ['-date'], 'verbose_name': 'Ошибка', 'verbose_name_plural': 'Ошибки'},
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='error_message',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Сообщение об ошибке'),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='stack_trace',
            field=models.TextField(blank=True, null=True, verbose_name='Трассировка'),
        ),
        migrations.AlterField(
            model_name='ourproduct',
            name='measure',
            field=models.CharField(choices=[('шт', 'штука'), ('кг', 'килограмм'), ('г', 'грамм'), ('л', 'литр')], default=('шт', 'штука'), max_length=4, verbose_name='Ед. измерения'),
        ),
    ]
