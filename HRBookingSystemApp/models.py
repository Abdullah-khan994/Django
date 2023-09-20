from django.db import models

# Create your models here.
        # Your custom logic after saving
class Contact(models.Model):
    # contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    desc=models.TextField(max_length=5000)
    phonenumber=models.IntegerField()
    def __str__(self):
        return self.name
    
class Room(models.Model):
    room_id = models.AutoField
    room_name = models.CharField(max_length=50)
    guests = models.IntegerField()
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=50, default="")
    sqft = models.IntegerField()
    desc = models.CharField(max_length=500)
    Price = models.IntegerField()
    Hotel_name = models.CharField(max_length=50)

    image = models.ImageField(upload_to='images/images')

    def __str__(self):
        return self.room_name

class Booking(models.Model):
    booker_id = models.AutoField
    booker_name = models.CharField(max_length=50)
    guests = models.IntegerField()
    category = models.CharField(max_length=100, default="")
    Price = models.IntegerField()
    Hotel_name = models.CharField(max_length=50)
    checkin_date = models.DateField()
    checkoutt_date = models.DateField()
    location = models.CharField(max_length=100, default="")
    status = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.booker_name
    

class Profiles(models.Model):
    Username = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    Phone = models.IntegerField()

    def __str__(self):
        return self.Username
    

class Feedback(models.Model):
    uname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    rateus = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.uname