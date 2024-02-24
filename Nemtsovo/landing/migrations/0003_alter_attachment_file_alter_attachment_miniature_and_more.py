# Generated by Django 5.0.1 on 2024-02-06 18:48

import django.core.validators
import landing.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_alter_attachment_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.ImageField(upload_to=landing.models.Attachment.get_upload_path, verbose_name='Фото/Видео'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='miniature',
            field=models.ImageField(blank=True, null=True, upload_to=landing.models.Attachment.get_miniature_upload_path, verbose_name='Миниатюра (опционально)'),
        ),
        migrations.AlterField(
            model_name='house',
            name='duration',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Продолжительность'),
        ),
    ]