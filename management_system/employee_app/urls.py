from django.contrib import admin
from django.urls import path,include
from employee_app import views

urlpatterns = [
 
    path('employee_add/',views.employee),
    path('employee_details/',views.employee_details),
    path('employee_update/<int:id>/',views.employee_update),
    path('employee_delete/<int:id>/',views.employee_delete),


]