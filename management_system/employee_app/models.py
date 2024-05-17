from django.db import models
# from app.models import CustomUser

# Create your models here.


class Employee_model(models.Model):

    # admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    GENDER = (

        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
    )

    DEEIGNATION = (

        ('Sales Officer', 'Sales Officer'),
        ('Territory Exceutive', 'Territory Exceutive'),
        ('Field Assistant', 'Field Assistant'),
        ('General Manager', 'General Manager'),
        ('HR Manager', 'HR Manager'),
        ('Office Management Staff', 'Office Management Staff'),
        ('CA', 'CA'),
        ('Director', 'Director'),
        ('Desk Office Assitant', 'Desk Office Assitant'),


    )
    profile_pic = models.ImageField(upload_to='media/profile_pic')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile_no = models.IntegerField(null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=100)
    designation = models.CharField(choices= DEEIGNATION, max_length=100)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    pan_card = models.ImageField(upload_to='media/pan_card')
    adhar_card = models.ImageField(upload_to='media/adhar_card')
    cheque = models.ImageField(upload_to='media/bank_details')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
