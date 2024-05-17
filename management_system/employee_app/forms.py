from django import forms
from .models import Employee_model


class employee_form(forms.ModelForm):
    class Meta:
        model = Employee_model
        fields = ('__all__')

        widgets = {

            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_no': forms.TextInput(attrs={'class': 'form-control','type':'number'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'designation': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'pan_card': forms.FileInput(attrs={'class': 'form-control'}),
            'adhar_card': forms.FileInput(attrs={'class': 'form-control'}),
            'cheque': forms.FileInput(attrs={'class': 'form-control'}),


        }
