# Generated by Django 3.1.5 on 2021-03-08 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0019_auto_20210309_0146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelreview',
            name='star',
        ),
    ]
