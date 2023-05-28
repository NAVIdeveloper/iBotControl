from django.urls import path,include
from .views import *


urlpatterns = [
    # path("register/",Api_Register,name='register'),
    path("login/",Api_Login,name='login'),
    # path("add-bot/",Api_add_bot),
    path("check-bot/",Api_check_bot),

    
]