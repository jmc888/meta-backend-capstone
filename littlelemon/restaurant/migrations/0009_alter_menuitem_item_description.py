# Generated by Django 5.0.6 on 2024-06-22 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_menuitem_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='item_description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]