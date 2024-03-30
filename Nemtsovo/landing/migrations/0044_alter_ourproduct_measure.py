# Generated by Django 5.0.1 on 2024-03-25 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0043_alter_attachment_file_alter_attachment_miniature_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourproduct',
            name='measure',
            field=models.CharField(choices=[('л', 'литр'), ('г', 'грамм'), ('шт', 'штука'), ('кг', 'килограмм')], default=('шт', 'штука'), max_length=4, verbose_name='Ед. измерения'),
        ),
    ]
