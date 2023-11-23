from django import forms
from django.forms import ModelForm
from .models import iplist

#Create a iplist form

class iplistForm(ModelForm):
    class Meta:
        model = iplist
        fields = ('group','ip_address','site','dept','user_name','mac_address')

        labels = {
            'group' : 'Group',
            'ip_address' :'',
            'site' : 'Site',
            'dept' :'',
            'user_name' : '',
            'mac_address' : '',

        }

        widgets = {
            
            # 'group' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Group'}),
            # 'group' : forms.ChoiceField( choices=[group_choices], required=False),
            'ip_address' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'IP Address'}),
            # 'site' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Site'}),
            'dept' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Dept'}),
            'user_name' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'UserName'}),
            'mac_address' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'MAC Address'}),
        }