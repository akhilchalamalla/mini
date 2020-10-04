from django.db import models
from django.contrib.auth.models import User,auth

# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
class Register(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    rollno=models.TextField()
    name=models.TextField()
    email=models.EmailField()
    year=models.TextField()
    branch=models.TextField()
    section=models.TextField()
    password=models.TextField()

class Eregister(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    rollno=models.TextField()
    email=models.EmailField()
    grade=models.TextField()
    backlogs=models.TextField()
    event=models.TextField()
    year=models.TextField()
    branch=models.TextField()
    section=models.TextField()

class Addevents(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    name=models.TextField()
    lastdate=models.DateField()
    eventdate=models.DateField()

class Status(models.Model):
    rollno=models.TextField()
    eventname=models.TextField()
    status=models.TextField()



   
            