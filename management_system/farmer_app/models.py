from django.db import models

# Create your models here.

class Farmer(models.Model):
    Name=models.CharField(max_length=50)
    Mobile_No=models.IntegerField(null=True , blank=True)
    Whatsapp_No=models.IntegerField(null=True , blank=True)
    Village=models.CharField(max_length=30)
    District=models.CharField(max_length=30)
    Pin_code=models.IntegerField(null=True , blank=True)
    created_employee = models.CharField(max_length=100)

