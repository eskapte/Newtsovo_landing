# Generated by Django 5.0.1 on 2024-02-24 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0022_alter_attachment_options_attachment_order_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='action',
            options={'ordering': ['order'], 'verbose_name': 'Досуг', 'verbose_name_plural': 'Досуг'},
        ),
        migrations.AlterModelOptions(
            name='house',
            options={'ordering': ['order'], 'verbose_name': 'Домик', 'verbose_name_plural': 'Домики'},
        ),
        migrations.AlterModelOptions(
            name='wellnesstreatment',
            options={'ordering': ['order'], 'verbose_name': 'Оздоровительная процедура', 'verbose_name_plural': 'Оздоровительные процедуры'},
        ),
        migrations.AlterField(
            model_name='action',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядок отображения'),
        ),
        migrations.AlterField(
            model_name='house',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядок отображения'),
        ),
        migrations.AlterField(
            model_name='ourproduct',
            name='measure',
            field=models.CharField(choices=[('шт', 'штука'), ('кг', 'килограмм'), ('г', 'грамм'), ('л', 'литр')], default=('шт', 'штука'), max_length=4, verbose_name='Ед. измерения'),
        ),
        migrations.AlterField(
            model_name='ourproduct',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядок отображения'),
        ),
        migrations.AlterField(
            model_name='wellnesstreatment',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядок отображения'),
        ),
    ]
