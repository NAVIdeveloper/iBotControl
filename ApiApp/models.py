from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=255,unique=True,null=True,blank=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255,unique=True)

class BotApp(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    bot_token = models.CharField(max_length=555,unique=True)
    register_date = models.DateTimeField(auto_now=True)

    timeline = models.DateTimeField(auto_now=True)
    telegram_admin = models.CharField(max_length=255)
    last_check = models.DateTimeField(auto_now=True)
    balans = models.FloatField(default=0.0)
    def __str__(self):
        return self.telegram_admin

class Ability(models.Model):
    icon_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()
    video_example = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class StartStep(models.Model):
    number = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='files')

    def __str__(self):
        return self.title



class Info(models.Model):
    logo = models.FileField(upload_to='files')
    name = models.CharField(max_length=255)
    slide_title = models.CharField(max_length=255)
    slide_text = models.CharField(max_length=255)
    slide_image = models.FileField(upload_to='files')
    abilitys = models.ManyToManyField(Ability)
    start_step = models.ManyToManyField(StartStep)

    def __str__(self):
        return self.name

class Doc(models.Model):
    title = models.CharField(max_length=255)
    text_1 = models.TextField(null=True,blank=True)
    text_2 = models.TextField(null=True,blank=True)
    video_url = models.CharField(max_length=255)
    program = models.FileField(upload_to='programs')

    def __str__(self):
        return self.title

class Pricing(models.Model):
    name = models.CharField(max_length=255)
    year = models.FloatField(default=0.5)
    text = models.TextField()

    def __str__(self):
        return self.name

class QueryAnswer(models.Model):
    query = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.query

class Contact(models.Model):
    ism = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.ism

class Command_Doc(models.Model):
    title=models.CharField(max_length=255)
    text = models.TextField()
    command = models.CharField(max_length=255)

    def __str__(self):
        return self.title

