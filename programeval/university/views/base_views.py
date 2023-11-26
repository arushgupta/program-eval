from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'programs': "Programs",
        'departments': "Departments"
    }
    return render(request, 'university/home.html', context)
