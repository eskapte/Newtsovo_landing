# Generated by Django 5.0.1 on 2024-03-08 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0036_rename_ourpets_ourpet_alter_ourproduct_measure'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ourpet',
            options={'ordering': ['order'], 'verbose_name': 'Питомец', 'verbose_name_plural': 'Питомцы'},
        ),
        migrations.AddField(
            model_name='ourpet',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядок отображения'),
        ),
        migrations.AlterField(
            model_name='ourproduct',
            name='measure',
            field=models.CharField(choices=[('кг', 'килограмм'), ('шт', 'штука'), ('г', 'грамм'), ('л', 'литр')], default=('шт', 'штука'), max_length=4, verbose_name='Ед. измерения'),
        ),
    ]
