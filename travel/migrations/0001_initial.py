# Generated by Django 5.0.2 on 2024-03-02 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=120)),
                ('email', models.CharField(max_length=100)),
                ('texts', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
