# Generated by Django 3.1.5 on 2021-03-04 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_auto_20210303_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='picture',
            field=models.ImageField(default='images/drug.gif', upload_to='images'),
        ),
    ]
