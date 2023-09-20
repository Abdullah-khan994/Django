from django.shortcuts import render
from HRBookingSystemApp.models import Contact,Room,Booking,Profiles,Feedback
from django.contrib import messages
from math import ceil


# Create your views here.

def index(request):
    return render(request, 'User/index.html')

def About(request):
    return render(request, 'User/About.html')

def Services(request):
    return render(request, 'User/Services.html')


def Feedbabck(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        email=request.POST.get("email")
        rateus=request.POST.get("rateus")
        desc=request.POST.get("desc")
        phone=request.POST.get("phone")
        myquery=Feedback(uname=uname, email=email, rateus=rateus, desc=desc, phone=phone)
        myquery.save()
        messages.info(request,"Thanks For The Feedback..")
        return render(request, 'User/feedback.html')
    
    return render(request, 'User/feedback.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        desc=request.POST.get("desc")
        pnumber=request.POST.get("pnumber")
        myquery=Contact(name=name, email=email, desc=desc, phonenumber=pnumber)
        myquery.save()
        messages.info(request,"We Will Get Back To You Soon..")
        return render(request, 'User/Contact.html')
    
    return render(request, 'User/Contact.html')

def Rooms(request):

    allRooms = []
    catrooms = Room.objects.values('category','id')
    cats = {item['category'] for item in catrooms}
    for cat in cats:
        room = Room.objects.filter(category=cat)
        n=len(room)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allRooms.append([room, range(1, nSlides), nSlides])

    params = {'allRooms':allRooms}
   
    return render(request, 'User/Rooms.html',params)


def Bookings(request):
    if request.method=="POST":
        booker_name = request.POST.get("booker_name")
        guests = request.POST.get("guests")
        category = request.POST.get("category")
        Price = request.POST.get("Price")
        Hotel_name = request.POST.get("Hotel_name")
        checkin_date = request.POST.get("checkin_date")
        checkoutt_date = request.POST.get("checkoutt_date")
        myquery1=Booking(booker_name=booker_name, guests=guests, category=category, Price=Price, Hotel_name=Hotel_name, checkin_date=checkin_date, checkoutt_date=checkoutt_date)
        myquery1.save()
        messages.info(request,"Your Booking is Done..")
        return render(request, 'User/Bookings.html')
    
    return render(request, 'User/Bookings.html')

def Bookingstatus(request):
    bookings = Booking.objects.all().order_by('-id').values()
    return render(request, 'User/Bookingstatus.html', {'bookings':bookings})

def Profile(request):
    if request.method=="POST":
        Username = request.POST.get("Username")
        Address = request.POST.get("Address")
        Phone = request.POST.get("Phone")
        myquery1=Profiles(Username=Username, Address=Address, Phone=Phone)
        myquery1.save()
        messages.info(request,"Profile Updated SuccessFully..")
        return render(request, 'User/Profile.html')
    
    profile = Profiles.objects.all()
    return render(request, 'User/profile.html', {'profile':profile})


