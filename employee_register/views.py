from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from employee_register.functions import handle_uploaded_file #functions.py
# Create your views here.

def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request,'employee_register/employee_list.html',context)

def employee_form(request):
    if request.method == "GET":
        form = EmployeeForm()
        return render(request,'employee_register/employee_form.html',{'form':form})
    else:
       form = EmployeeForm(request.POST, request.FILES)
       if  form.is_valid():
         handle_uploaded_file(request.FILES['file'])
         model_instance = form.save(commit=False)
         model_instance.save()
    return redirect('/employee/list')
def employee_delete(request):
    return