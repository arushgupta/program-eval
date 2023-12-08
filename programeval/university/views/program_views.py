from django.shortcuts import render, redirect, get_object_or_404
from university.models import Objective, Program, ProgramCourse, ProgramCourseObjective, ProgramObjective
from university.forms import AddProgramCourseObjectivesForm, AddProgramObjectivesForm, ProgramForm, ProgramCourseForm

def program_list(request):
    programs = Program.objects.all().order_by('name')
    return render(request, 'university/program/list.html', {'programs': programs})

def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    objectives = ProgramObjective.objects.filter(program_id=pk)
    program_courses = ProgramCourse.objects.filter(program=program)
    courses = []
    
    for program_course in program_courses:
        objective_ids = ProgramCourseObjective.objects.filter(program_course=program_course).values_list('objective_id', flat=True)
        course_objectives = Objective.objects.filter(id__in=objective_ids).order_by('id')
        if objectives.count() == 0:
            pair = (program_course, None)
        else:
            pair = (program_course, course_objectives)
        courses.append(pair)
        
    return render(request, 'university/program/detail.html', {'program': program, 'program_courses': courses, 'objectives': objectives})

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
    return render(request,'university/program/add_course.html',{'form': form, 'program': program})

def remove_courses(request, program_id, course_id):
    program_course = get_object_or_404(ProgramCourse, program_id=program_id, course_id=course_id)
    if request.method == 'POST':
        program_course.delete()
        return redirect('program-detail', program_id)
    return render(request,'university/program/remove_course.html',{'program_course': program_course , 'program': program_id})

def add_program_objective(request, program_id):
    program = get_object_or_404(Program, name=program_id)
    if request.method == 'POST':
        form = AddProgramObjectivesForm(program, request.POST)
        if form.is_valid():
            form.save()
            return redirect('program-detail', program_id)
    else:
        form = AddProgramObjectivesForm(program)
    return render(request, 'university/program/add_objective.html', {'form': form, 'program': program})

def remove_program_objective(request, program_id, objective_id):
    program_objective = get_object_or_404(ProgramObjective, program_id=program_id, objective_id=objective_id)
    if request.method == 'POST':
        program_objective.delete()
        return redirect('program-detail', program_id)
    return render(request, 'university/program/remove_objective.html', {'program_objective': program_objective})

def add_program_course_objective(request, program_id, course_id):
    program = get_object_or_404(Program, name=program_id)
    program_course = get_object_or_404(ProgramCourse, program=program, course_id=course_id)
    if request.method == 'POST':
        form = AddProgramCourseObjectivesForm(program, program_course, request.POST)
        if form.is_valid():
            form.save()
            return redirect('program-detail', program_id)
    else:
        form = AddProgramCourseObjectivesForm(program, program_course)
    return render(request, 'university/program/add_program_course_objective.html', {'form': form, 'program': program, 'program_course': program_course})

def delete_program_course_objective(request, program_id, course_id, objective):
    program_course = get_object_or_404(ProgramCourse, program_id=program_id, course_id=course_id)
    pc_objective = get_object_or_404(ProgramCourseObjective, program_course=program_course, objective__code=objective)
    if request.method == 'POST':
        pc_objective.delete()
        return redirect('program-detail', program_id)
    return render(request, 'university/program/remove_course_objective.html', {'program_course': program_course, 'pc_objective': pc_objective})
