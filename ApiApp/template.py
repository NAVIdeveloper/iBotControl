from django.urls import path,include
from .views import *

urlpatterns = [
    path("",Home_Page,name='home'),
    path("about/",About_Page,name='about'),
    path("pricing/",Pricing_Page,name='pricing'),
    path("contact/",Contact_Page,name='contact'),
    path("login/",Login_Page,name='login'),
    path("reg/",Reg_Page,name='reg'),
    path("logout/",Logout,name='logout'),
    path("profile/",Profile_Page,name='profile'),
]  

