# Generated by Django 5.0.1 on 2024-02-22 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0014_event_alter_action_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-date'],
            },
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['date'], 'verbose_name': 'Мероприятие', 'verbose_name_plural': 'Мероприятия'},
        ),
    ]