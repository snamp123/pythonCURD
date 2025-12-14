from django import forms
from .models import Employeespython

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employeespython
        fields = ['id','firstname', 'lastname']
