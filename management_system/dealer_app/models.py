from django.db import models

# Create your models here.

class Distributer(models.Model):
    Business_Name=models.CharField(max_length=50)
    Mobile_No=models.IntegerField(null=True,blank=True)
    Whatsapp_No=models.IntegerField(null=True , blank=True)
    Address=models.TextField(max_length=100)
    District=models.CharField(max_length=30)
    Pin_code=models.IntegerField(null=True , blank=True)
    Gst_No=models.CharField(max_length=30,null=True , blank=True)
    Seed_License=models.CharField(max_length=30,null=True , blank=True)
    created_employee = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Business_Name)

class Dealer(models.Model):
    authorized_distributor=models.ForeignKey(Distributer,on_delete=models.CASCADE,default = 1)
    Business_Name=models.CharField(max_length=50)
    Mobile_No=models.IntegerField(null=True,blank=True)
    Whatsapp_No=models.IntegerField(null=True , blank=True)
    Address=models.TextField(max_length=100)
    District=models.CharField(max_length=30)
    Pin_code=models.IntegerField(null=True , blank=True)
    Gst_No=models.CharField(max_length=30,null=True , blank=True)
    Seed_License=models.CharField(max_length=30,null=True , blank=True)
    created_employee = models.CharField(max_length=100)

    
    

