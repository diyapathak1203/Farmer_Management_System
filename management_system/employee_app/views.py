from django.shortcuts import render, redirect
from .forms import employee_form
from .models import Employee_model

# Create your views here.


def employee(request):

    if request.user.is_authenticated:

     if request.method == "POST":

        a = employee_form(request.POST, request.FILES)

        if a.is_valid():
            a.save()
            return redirect('/Admin/emp/employee_details/')

     a = employee_form()
     return render(request, 'employee/home.html', {'a': a})
    
    else:

        return redirect("/")


def employee_details(request):

    if request.user.is_authenticated:

     data = Employee_model.objects.all()

     return render(request, 'employee/view_employee.html', {'data': data})
    
    else:
       
       return redirect("/")


def employee_update(request, id):

    if request.user.is_authenticated:

     if request.method == "POST":

        data_form = employee_form(request.POST, request.FILES)

        data = Employee_model.objects.filter(id=id)
        if data_form.is_valid():

            for i in data:
                i.profile_pic = data_form.cleaned_data['profile_pic']
                i.first_name = data_form.cleaned_data['first_name']
                i.last_name = data_form.cleaned_data['last_name']
                i.mobile_no = data_form.cleaned_data['mobile_no']
                i.gender = data_form.cleaned_data['gender']
                i.designation = data_form.cleaned_data['designation']
                i.email = data_form.cleaned_data['email']
                i.address = data_form.cleaned_data['address']
                i.pan_card = data_form.cleaned_data['pan_card']
                i.adhar_card = data_form.cleaned_data['adhar_card']
                i.cheque = data_form.cleaned_data['cheque']
                i.save()

                return redirect('/Admin/emp/employee_details/')

     data = Employee_model.objects.filter(id=id)

     data_form = employee_form()

     gender = data_form["gender"]
 
     d = data_form["designation"]

     print(gender)
     print(d)
 
     return render(request, 'employee/update_employee.html', {'data': data, 'gender': gender, 'd': d})
    
    else:
       
       return redirect("/")


def employee_delete(request, id):

    if request.user.is_authenticated:

     data = Employee_model.objects.filter(id=id)
     data.delete()

     return redirect('/Admin/emp/employee_details/')
    
    else:
       
       return redirect("/")
