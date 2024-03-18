from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=15)

class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    Firstname=models.CharField(max_length=25)
    Lastname=models.CharField(max_length=25)
    Gender=models.CharField(max_length=10)
    Phoneno=models.BigIntegerField()
    Dob=models.DateField()
    Email=models.CharField(max_length=50)
    photo = models.FileField()

class Doctor(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=25)
    Lastname = models.CharField(max_length=25)
    place = models.CharField(max_length=25)
    Department = models.CharField(max_length=100)
    Qualification = models.CharField(max_length=100)
    Exprience = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Phoneno = models.BigIntegerField()
    Gender = models.CharField(max_length=10)
    Pwh = models.CharField(max_length=10)
    Dob = models.DateField()
    idproof=models.FileField()
    photo=models.FileField()

class Chat(models.Model):
    Fromid=models.ForeignKey(Login, on_delete=models.CASCADE,related_name="fid")
    Toid=models.ForeignKey(Login, on_delete=models.CASCADE,related_name="tid")
    Message=models.CharField(max_length=500)
    Date = models.DateField()
    Time=models.TimeField()


class Awareness(models.Model):
    Awarenes=models.CharField(max_length=1000)
    Details=models.CharField(max_length=1000)
    video=models.FileField()
    Date = models.DateField()