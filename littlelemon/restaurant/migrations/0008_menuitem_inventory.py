# Generated by Django 5.0.6 on 2024-06-22 09:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_alter_booking_reservation_slot_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='inventory',
            field=models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
