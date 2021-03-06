# Generated by Django 3.1.5 on 2021-03-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0013_hotelreview_picture'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='hotel',
            options={'verbose_name_plural': 'Hotels'},
        ),
        migrations.AlterModelOptions(
            name='hotelreview',
            options={'verbose_name_plural': 'Reviews'},
        ),
        migrations.AddField(
            model_name='hotelreview',
            name='review_type',
            field=models.CharField(choices=[('1', 'Show'), ('2', 'Hide')], default='1', max_length=128),
        ),
    ]
