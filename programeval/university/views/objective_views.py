from django.shortcuts import render, redirect, get_object_or_404
from university.models import Objective, SubObjective
from university.forms import AddObjectiveForm, AddSubObjectiveForm, UpdateObjectiveForm, UpdateSubObjectiveForm  

def objective_list(request):
    objectives = Objective.objects.all().order_by('code')
    return render(request, 'university/objective/list.html', {'objectives': objectives})

def objective_detail(request, code):
    objective = get_object_or_404(Objective, code=code)
    sub_objectives = SubObjective.objects.filter(objective=objective)
    return render(request, 'university/objective/detail.html', {'objective': objective, 'sub_objectives': sub_objectives})

def objective_create(request):
    if request.method == 'POST':
        form = AddObjectiveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('objective-list')
    else:
        form = AddObjectiveForm()
    return render(request, 'university/objective/create.html', {'form': form})

def objective_update(request, code):
    objective = get_object_or_404(Objective, code=code)
    if request.method == 'POST':
        form = UpdateObjectiveForm(objective, request.POST, instance=objective)
        if form.is_valid():
            form.save()
            return redirect('objective-detail', objective.code)
    else:
        form = UpdateObjectiveForm(objective, instance=objective)
    return render(request, 'university/objective/update.html', {'form': form})

def objective_delete(request, code):
    objective = get_object_or_404(Objective, code=code)
    if request.method == 'POST':
        objective.delete()
        return redirect('objective-list')
    return render(request, 'university/objective/delete.html', {'objective': objective})

def add_sub_objective(request, code):
    objective = get_object_or_404(Objective, code=code)
    if request.method == 'POST':
        form = AddSubObjectiveForm(objective, request.POST)
        if form.is_valid():
            form.save()
            return redirect('objective-detail', code)
    else:
        form = AddSubObjectiveForm(objective)
    return render(request, 'university/objective/add_sub_objective.html', {'form': form, 'objective': objective})

def update_sub_objective(request, o_code, s_code):
    objective = get_object_or_404(Objective, code=o_code)
    sub_objective = get_object_or_404(SubObjective, pk=s_code, objective=objective)
    if request.method == 'POST':
        form = UpdateSubObjectiveForm(objective, sub_objective, request.POST, instance=sub_objective)
        if form.is_valid():
            form.save()
            return redirect('objective-detail', o_code)
    else:
        form = UpdateSubObjectiveForm(objective, sub_objective, instance=sub_objective)
    return render(request, 'university/objective/update_sub_objective.html', {'form': form, 'objective': objective})

def delete_sub_objective(request, o_code, s_code):
    objective = get_object_or_404(Objective, code=o_code)
    sub_objective = get_object_or_404(SubObjective, pk=s_code, objective=objective)
    if request.method == 'POST':
        sub_objective.delete()
        return redirect('objective-detail', o_code)
    return render(request, 'university/objective/delete_sub_objective.html', {'objective': objective, 'sub_objective': sub_objective})
