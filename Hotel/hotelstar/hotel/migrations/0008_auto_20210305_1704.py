# Generated by Django 3.1.5 on 2021-03-05 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_contact_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='price',
            field=models.IntegerField(),
        ),
    ]
