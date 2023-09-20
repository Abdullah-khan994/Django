from django.urls import path
from HRBookingSystemAuth import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.handlelogin,name='handlelogin'),
    path('logout/',views.handlelogout,name='handlelogout'),
    path('authentication/activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='authentication/activate'),
]
