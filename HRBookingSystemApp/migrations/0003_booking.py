# Generated by Django 4.1.7 on 2023-08-17 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRBookingSystemApp', '0002_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=100)),
                ('Price', models.IntegerField()),
                ('Hotel_name', models.CharField(max_length=50)),
                ('checkin_date', models.DateField()),
                ('checkoutt_date', models.DateField()),
                ('guests', models.IntegerField()),
            ],
        ),
    ]
