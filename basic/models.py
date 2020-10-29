from django.db import models

# Create your models here.

class CallBack(models.Model):
    firstName = models.CharField(max_length=100 , null=True , blank=True)
    lastName = models.CharField(max_length=100 , null=True , blank=True)

   
    email = models.EmailField(max_length=100 , blank=True , null=True)

    number = models.CharField(max_length=10 , null=True , blank=True)

    


    