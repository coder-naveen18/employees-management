from django.shortcuts import render , get_object_or_404 , redirect
from .models import Employees_detail
from .forms import Add_Employee_form


# Create your views here.

def add_employee(request):
    if request.method == "POST":
        form = Add_Employee_form(request.POST , request.FILES)
        if form.is_valid():
            employee = form.save()
            return redirect('employees_detail')
    
    else :
        form = Add_Employee_form()
    return render(request, 'add_employee.html', {'form': form})


def get_details(request):
    employees = Employees_detail.objects.all()
    return render(request, "employees_detail.html", {'employees' : employees})


def employee_info(request, emp_id):
    info = get_object_or_404(Employees_detail, pk = emp_id)
    return render(request, "emp_info.html", {'info' : info})

def employee_delete(request, emp_id):
    employee = get_object_or_404(Employees_detail, pk = emp_id)
    
    if request.method == 'POST':
        employee.delete()
        return redirect('employees_detail')
    return render(request, 'employee_confirm_delete.html', {'employee': employee})

def edit_employee(request, emp_id):
    employee = get_object_or_404(Employees_detail, pk = emp_id)
    if request.method == 'POST':
         form = Add_Employee_form(request.POST , request.FILES, instance=employee)
         if form.is_valid():
             form.save()
             return redirect('employees_detail')

    else :
        form = Add_Employee_form(instance=employee)
    return render(request, 'add_employee.html', {'form': form})



