# Generated by Django 3.1.5 on 2021-03-03 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_auto_20210303_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hotel_type',
            field=models.CharField(choices=[('1', 'JIGRULI'), ('2', 'ARAJIGRULI')], default='1', max_length=128),
        ),
    ]
