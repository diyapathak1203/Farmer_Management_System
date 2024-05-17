from django import forms
from .models import Dealer

class DistributerForm(forms.Form):
    Business_Name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Mobile_No=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','type':'number'}))
    Whatsapp_No=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','type':'number'}),required=False)
    Address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    District=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Pin_code=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'number'}))
    Gst_No=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Seed_License=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))


class DealerForm(forms.ModelForm):

    class Meta:
        model=Dealer
        # print("this is id ",Distributer.id)
       
        fields=["authorized_distributor","Business_Name","Mobile_No","Whatsapp_No","Address","District","Pin_code","Gst_No","Seed_License"]
        widgets={

            'authorized_distributor':forms.Select(attrs={'class':'form-control'}),
            'Business_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Mobile_No':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'Whatsapp_No':forms.TextInput(attrs={'class':'form-control','type':'number','required': False}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),
            'District':forms.TextInput(attrs={'class':'form-control'}),
            'Pin_code':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'Gst_No':forms.TextInput(attrs={'class':'form-control'}),
            'Seed_License':forms.TextInput(attrs={'class':'form-control'}),
        }

    

