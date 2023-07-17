from django.db import models
from django.utils import timezone
# Create your models here.

class Service(models.Model):
    TYPE = (
       ('interieur', ('interieur')),
       ('exterieur', ('exterieur')))
        

    name= models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
       max_length=32,
       choices=TYPE,
       default='interieur',
       null=True, blank=True
   )
    image = models.ImageField(null= True, default ="service-1.jpg")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Client(models.Model):
    firstname= models.CharField(max_length=200)
    lasttname= models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    code_postal = models.CharField(max_length=10)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.firstname


class DemendeUnAppel(models.Model):
    name = models.CharField(max_length=200)
    email =models.EmailField(max_length=254)
    # service = models.ForeignKey(Service,on_delete=models.SET_NULL,null=True)
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    message = models.TextField(null=True,blank=True)
    

    def __str__(self):
        return self.name