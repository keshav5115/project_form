from django.db import models

# Create your models here.
class studentmodel(models.Model):
    stu_id=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phone=models.PositiveBigIntegerField()
    location=models.CharField(max_length=30)
    