from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employeespython
from .forms import EmployeeForm


# Create your views here.
def employee_list(request):
    employees = list(Employeespython.objects.all())
    #employees = Employeespython.objects.order_by('id')
    #employees = list(Employeespython.objects.all())
    #employees = Employeespython.objects.order_by('firstname')
    #return render(request, 'list.html', {'message': 'Hello, World with CURD!'})
    return render(request, 'employees/list.html', {'employees': employees})
