from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from university.forms import AddEvaluationForm
from university.models import ProgramCourse, Section, SectionEvaluation, SectionSubObjective


def program_course_section_detail(request, program_id, course_id, semester, year, section_code):
    program_course = get_object_or_404(ProgramCourse, program__name=program_id, course_id=course_id)
    section = get_object_or_404(Section, course_id=course_id, code=section_code, semester=semester, year=year)
    section_sub_objectives = SectionSubObjective.objects.filter(program_course=program_course, section=section)
    sso_evaluations = []
    for sso in section_sub_objectives:
        eval = SectionEvaluation.objects.filter(section_sub_objective=sso)
        if eval.count() == 0:
            sso_evaluations.append((sso, None))
        else:
            sso_evaluations.append((sso, eval.first()))
    return render(request, 'university/evaluation/section_objective.html', {'sso_evaluations': sso_evaluations, 'section': section, 'program_course': program_course})

@transaction.atomic
def add_evaluation(request, program_id, course_id, semester, year, section_code, sso_id):
    program_course = get_object_or_404(ProgramCourse, program__name=program_id, course_id=course_id)
    section = get_object_or_404(Section, course_id=course_id, code=section_code, semester=semester, year=year)
    section_sub_objective = get_object_or_404(SectionSubObjective, pk=sso_id)
    if request.method == 'POST':
        form = AddEvaluationForm(section_sub_objective, request.POST)
        if form.is_valid():
            evaluation = form.save()
            if evaluation:
                sso = evaluation.section_sub_objective
                sso.is_evaluated = True
                sso.save()
            return redirect('program_course_section-detail', program_id, course_id, semester, year, section_code)
    else:
        form = AddEvaluationForm(section_sub_objective)
    return render(request, 'university/evaluation/add_evaluation.html', {'form': form, 'sso': section_sub_objective})
