from django.shortcuts import render, redirect, get_object_or_404
from university.models import Department
from university.forms import DepartmentForm

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'university/department/department_list.html', {'departments': departments})

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'university/department/department_detail.html', {'department': department})

def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dept-list')
    else:
        form = DepartmentForm()
    return render(request, 'university/department/department_create.html', {'form': form})

def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('dept-detail', department.dept_code)
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'university/department/department_update.html', {'form': form})

def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('dept-list')
    return render(request, 'university/department/department_delete.html', {'department': department})

