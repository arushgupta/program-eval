from django.shortcuts import render
from university.forms import SemesterEvaluationForm
from university.models import Course, Department, Faculty, Program

# Create your views here.
def home(request):
    departments = Department.objects.all().count()
    programs = Program.objects.all().count()
    faculty = Faculty.objects.filter(is_active=True).count()
    courses = Course.objects.all().count()
    form = SemesterEvaluationForm()

    context = {
        'departments': departments,
        'programs': programs,
        'faculty': faculty,
        'courses': courses,
        'form': form
    }
    return render(request, 'university/home.html', context)
