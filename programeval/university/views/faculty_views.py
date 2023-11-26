from django.shortcuts import render, redirect, get_object_or_404
from university.models import Faculty
from university.forms import FacultyForm

def faculty_list(request):
    faculty = Faculty.objects.filter(is_active=True)
    return render(request, 'university/faculty/list.html', {'faculty': faculty})

def faculty_detail(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    return render(request, 'university/faculty/detail.html', {'faculty': faculty})

def faculty_create(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty-list')
    else:
        form = FacultyForm()
    return render(request, 'university/faculty/create.html', {'form': form})

def faculty_update(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk, is_active=True)
    if request.method == 'POST':
        form = FacultyForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('faculty-detail', faculty.uni_id)
    else:
        form = FacultyForm(instance=faculty)
    return render(request, 'university/faculty/update.html', {'form': form})

def faculty_fire(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        faculty.is_active = False
        faculty.save()
        return redirect('faculty-list')
    return render(request, 'university/faculty/fire.html', {'faculty': faculty})