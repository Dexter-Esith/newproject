# Generated by Django 3.1.5 on 2021-03-05 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_auto_20210305_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hotel_type2',
            field=models.CharField(choices=[('1', 'Free Parking'), ('2', 'No Parking')], default=1, max_length=128),
        ),
    ]
