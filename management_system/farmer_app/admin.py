from django.contrib import admin

from .models import Farmer

# Register your models here.

@admin.register(Farmer)

class farmerAdmin(admin.ModelAdmin):
    list_display=['id','Name','Mobile_No','Whatsapp_No','Village','District','Pin_code']

