from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.

class Connection(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobilenumber=models.CharField(max_length=10)
    GENDER_CHOICES=(("Male","Male"),("Female","Female"),("Other","Other"))
    gender=models.CharField(max_length=50,choices=GENDER_CHOICES,default="other")
    MARRIED_CHOICES=(("Married","Married"),("Single","Single"))
    marriedstatus=models.CharField(max_length=50,choices=MARRIED_CHOICES,default="single")
    adharno=models.CharField(max_length=12)
    address=models.CharField(max_length=50)
    applieddate=models.DateTimeField(auto_now_add=True)
    zipcode=models.IntegerField()

    def __str__(self):
        return self.name

        
    
'''
class Bookc(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    GAS_CHOICES=((14.2,"14.2"),(5,"5"),(30,"30"),)
    gasbook=models.FloatField(max_length=9,choices=GAS_CHOICES,default=5)
    date=models.DateTimeField()

    def __str__(self):
        return self.title

'''

class BookGas(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    connection = models.ForeignKey('Connection', on_delete=models.CASCADE)

    GAS_CHOICES=((14.2,"14.2"),(5,"5"),(30,"30"))
    cylinder_KG=models.FloatField(max_length=9,choices=GAS_CHOICES,default=5)
    STATUS_CHOICES=(("confirmed","Confirmed"),('On the way','On the way'),('Delivered','Delivered'))
    status=models.CharField(max_length=100,default='In Progress',choices=STATUS_CHOICES)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date
        
        

    
