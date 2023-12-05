from django.shortcuts import render, redirect, get_object_or_404
from university.models import Objective, ProgramCourseObjective, Course, ProgramCourse
from university.forms import AddObjectiveForm, UpdateObjectiveForm  

def objective_list(request):
    objectives = Objective.objects.all().order_by('code')
    return render(request, 'university/objective/list.html', {'objectives': objectives})

def objective_detail(request, pk):
    objective = get_object_or_404(Objective, pk=pk)
    return render(request, 'university/objective/detail.html', {'objective': objective})

def objective_create(request):
    if request.method == 'POST':
        form = AddObjectiveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('objective-list')
    else:
        form = AddObjectiveForm()
    return render(request, 'university/objective/create.html', {'form': form})

def objective_update(request, pk):
    objective = get_object_or_404(Objective, pk=pk)
    if request.method == 'POST':
        form = UpdateObjectiveForm(request.POST, instance=objective)
        if form.is_valid():
            form.save()
            return redirect('objective-detail', objective.pk)
    else:
        form = UpdateObjectiveForm(instance=objective)
    return render(request, 'university/objective/update.html', {'form': form})

def objective_delete(request, pk):
    objective = get_object_or_404(Objective, pk=pk)
    if request.method == 'POST':
        objective.delete()
        return redirect('objective-list')
    return render(request, 'university/objective/delete.html', {'objective': objective})

def assign_objective_to_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        objective_id = request.POST.get('objective_id')
        objective = get_object_or_404(Objective, pk=objective_id)
        ProgramCourseObjective.objects.create(course=course, objective=objective)
        return redirect('course-detail', course_id)
    objectives = Objective.objects.exclude(program_courses__course=course)
    return render(request, 'university/objective/assign_to_course.html', {'course': course, 'objectives': objectives})
