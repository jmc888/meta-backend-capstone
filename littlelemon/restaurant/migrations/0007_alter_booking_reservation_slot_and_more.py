# Generated by Django 5.0.6 on 2024-06-22 09:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_alter_booking_reservation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='reservation_slot',
            field=models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(11), django.core.validators.MaxValueValidator(19)]),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='item_description',
            field=models.CharField(default='', max_length=255),
        ),
    ]
