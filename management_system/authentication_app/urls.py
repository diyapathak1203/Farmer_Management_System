from django.contrib import admin
from django.urls import path,include
from authentication_app import views

urlpatterns = [
 
    path('employee_register/',views.employee_register),
    path('',views.loginhandle),
    path('logout/',views.logouthandle),
    path('profile_update/<int:id>/',views.profileUpdate)



]