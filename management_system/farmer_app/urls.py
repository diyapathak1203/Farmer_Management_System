from django.contrib import admin
from django.urls import path,include
from farmer_app import views

urlpatterns = [
 
    path('farmer_form/',views.farmer_detail),
    path('farmer/update/<int:id>/',views.update),
    path('farmer/delete/<int:id>/',views.delete),
   

]