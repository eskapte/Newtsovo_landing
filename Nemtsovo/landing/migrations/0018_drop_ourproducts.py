from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0017_ourproduct_is_available'),
    ]

    operations = [
        migrations.DeleteModel('OurProduct', )
    ]
