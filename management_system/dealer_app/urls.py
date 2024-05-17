from django.contrib import admin
from django.urls import path,include
from dealer_app import views

urlpatterns = [
 
    path('dealer_detail/',views.dealer),
    path('dealer_form/',views.dealer_form),
    path('distributer_form/',views.Distributers),
    path('distributer_detail/',views.distributer_object),
    path('dealer_delete/<int:id>/',views.delete_data),
    path('dealer_update/<int:id>/',views.update_data),
    path('distributer_delete/<int:id>/',views.Distributer_delete_data),
    path('distributer_update/<int:id>/',views.Distributer_update_data),

]