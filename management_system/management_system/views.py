from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
# from app.EmailBackEnd import EmailBackEnd
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from management_system import views

# from app.models import CustomUser


def BASE(request):

    if request.user.is_authenticated:

     return render(request, 'base.html')
    
    else:
       
       return redirect("/")


# def LOGIN(request):
#     return render(request, 'login.html')


# def doLogin(request):
#     if request.method == "POST":
#         user = EmailBackEnd.authenticate(request, username=request.POST.get('email'),
#                                          password=request.POST.get('password'))
#         if user != None:
#             login(request, user)
#             user_type = user.user_type
#             if user_type == '1':
#                 return redirect('admin_home')
#             elif user_type == '2':
#                 return redirect('manager_home')
#             elif user_type == '3':
#                 return redirect('employee_home')
#             else:
#                 # message
#                 messages.error(request, 'Email and Password are invalid!')
#                 return redirect('login')

#         else:
#             # message
#             messages.error(request, 'Email and Password are invalid!')
#             return redirect('login')


def doLogout(request):

    if request.user.is_authenticated:
     logout(request)
     return redirect('login')
    else:

        return redirect("/")


def PROFILE(request):

    if request.user.is_authenticated:
     user = CustomUser.objects.get(id=request.user.id)

     context = {
        "user": user,
     }
     return render(request, 'profile.html', context)
    
    else:

        return redirect("/")


def PROFILE_UPDATE(request):

    if request.user.is_authenticated:
     
     if request.method == "POST":
        profile_pic =request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # email == request.POST.get('email')
        # username == request.POST.get('username')
        password = request.POST.get('password')

     try:
        customuser = CustomUser.objects.get(id=request.user.id)
        customuser.first_name = first_name
        customuser.last_name = last_name
        customuser.profile_pic = profile_pic
        if (password!= None) and (password!= ""):
            customuser.set_password(password)
        if (profile_pic!= None) and (profile_pic!= ""):
            customuser.profile_pic=profile_pic
        customuser.save()
        messages.success(request, "Profile updated successfully!")
        redirect('profile')
     except:
        messages.error(request, 'Failed to update profile!')

     return render(request, 'profile.html')
    
    else:
        return redirect("/")





