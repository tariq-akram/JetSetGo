# Generated by Django 5.0 on 2024-03-14 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0015_bookinghistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupbooking',
            name='group_name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
