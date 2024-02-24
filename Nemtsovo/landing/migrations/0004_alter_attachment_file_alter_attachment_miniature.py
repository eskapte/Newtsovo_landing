# Generated by Django 5.0.1 on 2024-02-06 19:26

import landing.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_alter_attachment_file_alter_attachment_miniature_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(upload_to=landing.models.Attachment.get_upload_path, verbose_name='Фото/Видео'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='miniature',
            field=models.FileField(blank=True, null=True, upload_to=landing.models.Attachment.get_miniature_upload_path, verbose_name='Миниатюра (опционально)'),
        ),
    ]
