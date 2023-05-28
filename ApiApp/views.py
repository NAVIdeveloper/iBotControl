from django.shortcuts import render,redirect

from .models import *
from .serializer import *
from django.contrib.auth import login,logout
# Create your views here.
# from django.db.models import Max,Min,Q as SearchQ

from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes,action
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
import datetime


@api_view(['POST'])
def Api_Login(request):
    data = request.data
    try:
        print(data)
        email = data['email']
        password = data['password']
        user = User.objects.get(email=email)
        if user.check_password(password):
            token = Token.objects.get(user=user)
            DATA = {
                "status":True,
                "token":token.key,
            }
            return Response(DATA)
    except Exception as r:
        print(r)
    DATA = {
        "status":False,
    }
    return Response(DATA)


@api_view(['POST'])
def Api_check_bot(request):
    data = request.data
    print(data)
    user = data['user']
    try:
        user=Token.objects.get(key=user).user
        app = BotApp.objects.get(user=user)
        app.last_check = datetime.datetime.now()
        app.save()
        days = datetime.datetime.now().date()-app.timeline.date()
        if days.days > 0:
            DATA = {
                "status":True,
                "bot_token":app.bot_token,
                "telegram_admin":app.telegram_admin,
            }
        else:
            DATA = {
                "status":True,
                "bot_token":app.bot_token,
                "telegram_admin":app.telegram_admin,
            }
        return Response(DATA)

    except Exception as r:
        print(r)
        DATA = {
            "status":False,
        }
        return Response(DATA)


def Home_Page(request):
    DATA = {
        "info":Info.objects.last(),
        "count_step":len(Info.objects.last().start_step.all())
    }

    return render(request,'index.html',DATA)

def About_Page(request):
    DATA = {
        "info":Info.objects.last(),
        "docs":Doc.objects.all(),
    }

    return render(request,'features.html',DATA)

def Pricing_Page(request):
    DATA = {
        "info":Info.objects.last(),
        "pricing":Pricing.objects.all(),
        "querys":QueryAnswer.objects.all().order_by("-id"),
    }
    return render(request,"pricing.html",DATA)

def Contact_Page(request):
    DATA = {
        "info":Info.objects.last(),
    }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        c = Contact.objects.create(ism=name,contact=email,message=message)
        return redirect('home')
    
    return render(request,'contact.html',DATA)

def Login_Page(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    DATA = {
        "info":Info.objects.last(),
    }
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user=User.objects.get(email=email)
            if user.check_password(password):
                login(request,user)
                return redirect('login')
        except Exception as r:
            print(r)
    return render(request,"login.html",DATA)

def Reg_Page(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    DATA = {
        "info":Info.objects.last(),
    }
    if request.method == 'POST':
        username = request.POST['username']
        bot_token = request.POST['bot_token']
        email = request.POST['email']
        admin = request.POST['admin']
        password = request.POST['password']
        timeline = datetime.datetime.now()+datetime.timedelta(days=7)
        try:
            user=User.objects.create(email=email,username=username)
            user.set_password(password)
            user.save()
            token=Token.objects.create(user=user)
            bot = BotApp.objects.create(user=user,bot_token=bot_token,telegram_admin=admin,timeline=timeline)
            login(request,user)
            return redirect('reg')
        except Exception as r:
            print(r)
    return render(request,"signup.html",DATA)

def Logout(request):
    logout(request)

    return redirect("login")

def Profile_Page(request):
    if request.user.is_authenticated == False:
        return redirect('home')
    
    DATA = {
        "info":Info.objects.last(),
        "user":request.user,
        "bot":BotApp.objects.get(user=request.user),
    }
    return render(request,'profile/index.html',DATA)

