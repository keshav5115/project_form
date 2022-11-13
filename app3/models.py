from django.db import models

# Create your models here.
from django.contrib.auth.models import User,AbstractUser

# Create your models here.
class studentmodel(User):
    
    
    phone=models.PositiveBigIntegerField()
    gender=models.CharField(max_length=25,choices=[['male','Male'],['female','Female']])