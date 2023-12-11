from django.shortcuts import render
from university.forms import SemesterEvaluationForm, YearlyEvaluationForm
from university.models import Course, Department, Faculty, Program

# Create your views here.
def home(request):
    departments = Department.objects.all().count()
    programs = Program.objects.all().count()
    faculty = Faculty.objects.filter(is_active=True).count()
    courses = Course.objects.all().count()
    semester_form = SemesterEvaluationForm()
    yearly_form = YearlyEvaluationForm()

    context = {
        'departments': departments,
        'programs': programs,
        'faculty': faculty,
        'courses': courses,
        'semester_form': semester_form,
        'yearly_form': yearly_form
    }
    return render(request, 'university/home.html', context)
