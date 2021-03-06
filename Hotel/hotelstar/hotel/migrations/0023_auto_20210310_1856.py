# Generated by Django 3.1.5 on 2021-03-10 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0022_auto_20210309_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelreview',
            name='comment',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='hotelreview',
            name='email',
            field=models.EmailField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='hotelreview',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='hotelreview',
            name='permission',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='hotelreview',
            name='picture',
            field=models.ImageField(default='bendu.jpg', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='hotelreview',
            name='rating_number',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='5', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='hotelreview',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel'),
        ),
    ]
