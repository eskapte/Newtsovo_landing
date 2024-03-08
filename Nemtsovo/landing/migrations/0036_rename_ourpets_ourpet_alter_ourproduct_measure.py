# Generated by Django 5.0.1 on 2024-03-08 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0035_ourpets_alter_booking_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OurPets',
            new_name='OurPet',
        ),
        migrations.AlterField(
            model_name='ourproduct',
            name='measure',
            field=models.CharField(choices=[('г', 'грамм'), ('кг', 'килограмм'), ('шт', 'штука'), ('л', 'литр')], default=('шт', 'штука'), max_length=4, verbose_name='Ед. измерения'),
        ),
    ]