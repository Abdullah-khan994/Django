# Generated by Django 4.1.7 on 2023-08-17 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRBookingSystemApp', '0004_rename_booking_name_booking_booker_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
    ]