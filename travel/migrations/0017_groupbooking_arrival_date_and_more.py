# Generated by Django 5.0 on 2024-03-14 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0016_groupbooking_group_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupbooking',
            name='arrival_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='groupbooking',
            name='departure_date',
            field=models.DateField(default=None),
        ),
    ]
