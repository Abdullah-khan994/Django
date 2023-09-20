from django.contrib import admin
from HRBookingSystemApp.models import Contact,Room,Booking,Profiles,Feedback
# Register your models here.
admin.site.register(Contact)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Profiles)
admin.site.register(Feedback)