# Generated by Django 5.0 on 2024-03-14 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0013_itinerary_delete_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itinerary',
            old_name='users',
            new_name='user',
        ),
    ]
