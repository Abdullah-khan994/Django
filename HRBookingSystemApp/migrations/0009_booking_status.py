# Generated by Django 4.1.7 on 2023-08-18 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRBookingSystemApp', '0008_remove_profiles_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(default='', max_length=100),
        ),
    ]
