from django.shortcuts import render, redirect, get_object_or_404
from university.models import Program, ProgramCourse
from university.forms import ProgramForm, ProgramCourseForm

def program_list(request):
    programs = Program.objects.all().order_by('name')
    return render(request, 'university/program/list.html', {'programs': programs})

def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    courses = ProgramCourse.objects.filter(program_id=pk)
    return render(request, 'university/program/detail.html', {'program': program, 'program_courses': courses})

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

def list_courses(request, program_id):
    program_courses = ProgramCourse.objects.filter(program_id=program_id)
    return render(request, 'university/program/list_courses.html', {'program_courses': program_courses, 'program': program_id})

def add_courses(request, program_id):
    program = get_object_or_404(Program, name=program_id)
    if request.method =='POST':
        form = ProgramCourseForm(program.department, program_id, request.POST)
        if form.is_valid():
            form.save()
            return redirect('program-detail', program_id)
    else:
        form = ProgramCourseForm(program.department, program_id)
    return render(request,'university/program/add_course.html',{'form': form, 'program': program_id})

def remove_courses(request, program_id, course_id):
    program_course = get_object_or_404(ProgramCourse, program_id=program_id, course_id=course_id)
    if request.method == 'POST':
        program_course.delete()
        return redirect('program-detail', program_id)
    return render(request,'university/program/remove_course.html',{'program_course': program_course , 'program': program_id})
