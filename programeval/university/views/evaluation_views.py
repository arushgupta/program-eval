from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from university.views.base_views import home
from university.forms import AddEvaluationForm, SemesterEvaluationForm, UpdateEvaluationForm
from university.models import ProgramCourse, ProgramCourseObjective, ProgramObjective, Section, SectionEvaluation, SectionSubObjective, SubObjective

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

def edit_evaluation(request, program_id, course_id, semester, year, section_code, sso_id):
    section_sub_objective = get_object_or_404(SectionSubObjective, pk=sso_id)
    section_evaluation = get_object_or_404(SectionEvaluation, section_sub_objective=section_sub_objective)
    if request.method == 'POST':
        form = UpdateEvaluationForm(section_sub_objective, request.POST, instance=section_evaluation)
        if form.is_valid():
            form.save()
            return redirect('program_course_section-detail', program_id, course_id, semester, year, section_code)
    else:
        form = UpdateEvaluationForm(section_sub_objective, instance=section_evaluation)
    return render(request, 'university/evaluation/update_evaluation.html', {'form': form, 'sso': section_sub_objective, 'program_id': program_id, 'course_id': course_id, 'semester': semester, 'year': year, 'section_code': section_code})

@transaction.atomic
def delete_evaluation(request, program_id, course_id, semester, year, section_code, sso_id):
    section_sub_objective = get_object_or_404(SectionSubObjective, pk=sso_id)
    section_evaluation = get_object_or_404(SectionEvaluation, section_sub_objective=section_sub_objective)
    if request.method == 'POST':
        section_sub_objective.is_evaluated = False
        section_sub_objective.save()
        section_evaluation.delete()
        return redirect('program_course_section-detail', program_id, course_id, semester, year, section_code)
    return render(request, 'university/evaluation/delete_evaluation.html', {'sso': section_sub_objective, 'program_id': program_id, 'course_id': course_id, 'semester': semester, 'year': year, 'section_code': section_code})

def get_semester_program_evaluation(request):
    form = SemesterEvaluationForm(request.POST)
    
    if form.is_valid():
        pass
    
    program = form.cleaned_data['program']
    semester = int(form.cleaned_data['semester'])
    year = form.cleaned_data['year']
    program_courses = ProgramCourse.objects.filter(program=program)
    
    result = []
    
    for program_course in program_courses:
        sections = Section.objects.filter(course=program_course.course, semester=semester, year=year)
        section_objectives = []

        if sections.count() > 0:
            for section in sections:
                section_sub_objectives = SectionSubObjective.objects.filter(program_course=program_course, section=section)
                section_evaluations = []
                
                if section_sub_objectives.count() > 0:
                    for section_so in section_sub_objectives:
                        evaluation = SectionEvaluation.objects.filter(section_sub_objective=section_so)
                        if evaluation.count() == 0:
                            section_evaluations.append((section_so, None))
                        else:
                            section_evaluations.append((section_so, evaluation.first()))
            
                    section_objectives.append((section, section_evaluations))
                else:
                    section_objectives.append((section, None))
            result.append((program_course, section_objectives))
        else:
            result.append((program_course, None))

    semester = f"{Section.Semester(semester).label} {year}"
    return render(request, 'university/evaluation/semester_evaluation.html', {'program': program, 'semester': semester, 'program_courses': program_courses, 'program_course_evaluations': result})

    
