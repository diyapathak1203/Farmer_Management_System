from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from farmer_app.forms import EmployeeForm
from dealer_app.forms import DealerForm, DistributerForm
from dealer_app.models import Dealer, Distributer
# from app.models import CustomUser
from django.db.models import Q
from employee_app.models import Employee_model
from farmer_app.models import Farmer
from app.models import Resourse


@login_required(login_url='/')
def HOME(request):

    if request.user.is_authenticated:

     farmer_count = Farmer.objects.all().count()
     dealer_count = Dealer.objects.all().count()
     distributor_count = Distributer.objects.all().count()
     employee_count = Employee_model.objects.all().count()

     context = {
        'farmer_count': farmer_count,
        'dealer_count': dealer_count,
        'distributor_count': distributor_count,
        'employee_count': employee_count,
     }

     return render(request, 'admin/home.html', context)
    
    else:
       
       return redirect("/")


@login_required(login_url='/')
def ADD_FARMER(request):

    if request.user.is_authenticated:

     farmer = EmployeeForm()
     return render(request, 'admin/add_farmer.html', {'farmer': farmer})
    
    else:
       
       return redirect("/")


@login_required(login_url='/')
def ADD_DISTRIBUTOR(request):

    if request.user.is_authenticated:

     a = DistributerForm()
     return render(request, 'admin/add_distributor.html', {'a': a})
    
    else:
       
       return redirect("/")


def ADD_DEALER(request):

    if request.user.is_authenticated:

     a = DealerForm()
     return render(request, 'admin/add_dealer.html', {'a': a})
    
    else:

        return redirect("/")


def VIEW_EMPLOYEE(request):

    if request.user.is_authenticated:

     return render(request, 'admin/view_employee.html')
    
    else:

        return redirect("/")


def VIEW_FARMER(request):

    if request.user.is_authenticated:

     all = Farmer.objects.all()
     return render(request, 'admin/view_farmer.html', {'all': all})
    
    else:

        return redirect("/")


def VIEW_DEALER(request):

    if request.user.is_authenticated:

     dealer = Dealer.objects.all()
     return render(request, 'admin/view_dealer.html', {'dealer': dealer})
    
    else:
       
       return redirect("/")


def VIEW_DISTRIBUTOR(request):

    if request.user.is_authenticated:

     distributer = Distributer.objects.all()
     return render(request, 'admin/view_distributor.html', {'distributer': distributer})
    
    else:
       
       return redirect("/")


def RESOURCES(request):

    if request.user.is_authenticated:

     a = Resourse.objects.all()
     print(a)
     return render(request, 'admin/resources.html', {'a': a})
    
    else:
       
       return redirect("/")


def search(request):

    if request.user.is_authenticated:

     if 'q' in request.GET:
        q = request.GET['q']
        farmer_q = Q(Q(Name__icontains=q))
        dealer_q = Q(Q(Business_Name__icontains=q))
        distributer_q = Q(Q(Business_Name__icontains=q))

        all = Farmer.objects.filter(farmer_q)
        print("all", len(all))
        dealer = Dealer.objects.filter(dealer_q)
        print("dealer", len(dealer))
        distributer = Distributer.objects.filter(distributer_q)
        print("distributer", len(distributer))

        if (len(all) != 0):
            return render(request, 'admin/view_farmer.html', {'all': all})

        if (len(dealer) != 0):
            return render(request, 'admin/view_dealer.html', {'dealer': dealer})

        elif (len(distributer) != 0):
            return render(request, 'admin/view_distributor.html', {'distributer': distributer})

        else:
            messages.error(request, 'Item not found')
            return render(request, 'search.html')
        
    else:
       
       return redirect("/")
