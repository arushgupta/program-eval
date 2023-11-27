from django.shortcuts import render, redirect, get_object_or_404
from university.models import Program
from university.forms import AddProgramForm

def program_list(request):
    programs = Program.objects.filter(is_active=True)
    return render(request, 'university/program/list.html', {'programs': programs})

def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'university/program/detail.html', {'program': program})

def program_create(request):
    if request.method == 'POST':
        form = AddProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('program-list')
    else:
        form = AddProgramForm()
    return render(request, 'university/program/create.html', {'form': form})

def program_update(request, pk):
    program = get_object_or_404(Program, pk=pk, is_active=True)
    if request.method == 'POST':
        form = AddProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('faculty-detail', program.uni_id)
    else:
        form = AddProgramForm(instance=program)
    return render(request, 'university/program/update.html', {'form': form})

def program_delete(request, pk):
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        program.delete()
        return redirect('program-list')
    return render(request, 'university/program/fire.html', {'program': program})