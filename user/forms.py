from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        # fields = '__all__'
        fields = ['type','brand','model','owner_name','registration_number','date_of_registration','description',]

