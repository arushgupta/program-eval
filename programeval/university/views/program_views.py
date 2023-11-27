from django.shortcuts import render, redirect, get_object_or_404
from university.models import Program
from university.forms import ProgramForm

def program_list(request):
    programs = Program.objects.all()
    return render(request, 'university/program/list.html', {'programs': programs})

def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'university/program/detail.html', {'program': program})

def program_create(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('program-list')
    else:
        form = ProgramForm()
    return render(request, 'university/program/create.html', {'form': form})

def program_update(request, pk):
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('program-detail', program.name)
    else:
        form = ProgramForm(instance=program)
    return render(request, 'university/program/update.html', {'form': form})

def program_delete(request, pk):
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        program.delete()
        return redirect('program-list')
    return render(request, 'university/program/delete.html', {'program': program})
