from django.urls import path
from HRBookingSystemApp import views

urlpatterns = [
     path('', views.index, name='index'),
    path('About', views.About, name='About'),
    path('Services', views.Services, name='Services'),
    path('Contact', views.contact, name='Contact'),
    path('Rooms', views.Rooms, name='Rooms'),
    path('Bookings', views.Bookings, name='Bookings'),
    path('Bookingstatus', views.Bookingstatus, name='Bookingstatus'),
    path('Profile', views.Profile, name="Profile"),
    path('Feedback', views.Feedbabck, name="Feedback"),
    
]