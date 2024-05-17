from django.shortcuts import render, HttpResponse, redirect
from .forms import employee_register_form
# from django.contrib.auth.forms import AuthenticationForm
from .forms import employee_login_form
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.


def employee_register(request):

    if request.method == "POST":
        a = employee_register_form(request.POST)

        print(a)

        if a.is_valid():
            a.save()
            return redirect("/")

    a = employee_register_form()

    return render(request, 'signup.html', {'a': a})


def loginhandle(request):

    if request.method == "POST":

        data = employee_login_form(data=request.POST)
        print(data)

        if data.is_valid():

            print("I am enter")

            uname = data.cleaned_data['username']
            print(uname)
            paasw = data.cleaned_data['password']
            print(paasw)
            myuser = authenticate(username=uname, password=paasw)

            print(myuser)

            if myuser is not None:

                login(request, myuser)

                return redirect('admin_home')

    else:

        data = employee_login_form()

    return render(request, 'login.html', {'data': data})


def logouthandle(request):

    if request.user.is_authenticated:

        logout(request)

        return redirect("/")

    else:

        return redirect("/")


def profileUpdate(request, id):

    if request.user.is_authenticated:

     if request.method == "POST":

        user = User.objects.filter(id=id)

        for i in user:
         i.username = request.POST['username']
         i.email = request.POST['email']
         i.password1 = request.POST['password1']
         i.password2 = request.POST['password2']
         i.save()

         return redirect("/Admin/Home")

     user = User.objects.filter(id=id)
     return render(request, 'profile.html', {'user': user})
    
    return redirect("/")
