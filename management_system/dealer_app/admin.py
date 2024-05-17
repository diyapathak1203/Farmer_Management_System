from django.contrib import admin
from .models import Dealer,Distributer

# Register your models here.



@admin.register(Distributer)

class DealerAdmin(admin.ModelAdmin):
    list_display=["id","Business_Name","Mobile_No","Whatsapp_No","Address","District","Pin_code","Gst_No","Seed_License"]




@admin.register(Dealer)

class farmerAdmin(admin.ModelAdmin):
    list_display=["id","authorized_distributor","Business_Name","Mobile_No","Whatsapp_No","Address","District","Pin_code","Gst_No","Seed_License"]



