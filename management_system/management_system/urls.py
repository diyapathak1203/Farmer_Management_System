"""management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from management_system import views, admin_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),

    # login path
    path('', include('authentication_app.urls'), name='login'),
    # path('doLogin', views.doLogin, name='doLogin'),

    # logout path
    # path('doLogout', views.doLogout, name='logout'),


    # signup



    # profile update
    path('Profile', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),


    # Admin Panel addd

    path('Admin/Home', admin_views.HOME, name='admin_home'),
    path('Admin/Farmer/Add', admin_views.ADD_FARMER, name="add_farmer"),
    path('Admin/Distributor/Add',admin_views.ADD_DISTRIBUTOR, name="add_distributor"),
    path('Admin/Dealer/Add', admin_views.ADD_DEALER, name="add_dealer"),


    path('Admin/Employee/View',admin_views.VIEW_EMPLOYEE, name="view_employee"),
    path('Admin/Farmer/View',admin_views.VIEW_FARMER, name="view_farmer"),
    path('Admin/Dealer/View',admin_views.VIEW_DEALER, name="view_dealer"),
    path('Admin/Distributor/View',admin_views.VIEW_DISTRIBUTOR, name="view_distributor"),
    path('Admin/Resources', admin_views.RESOURCES, name='resources'),



    # main dealer distributer farmer url
    path('Admin/deal/',include('dealer_app.urls')),
    path('Admin/farm/',include('farmer_app.urls')),
    path('Admin/emp/',include('employee_app.urls')),


    path('Admin/auth/',include('authentication_app.urls')),
    
    
   

   
    
       
    #employee panel


    path('search/',admin_views.search),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

