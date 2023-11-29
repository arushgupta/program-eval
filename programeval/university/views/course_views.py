from university.models import Course
from university.forms import CourseForm
from django.shortcuts import redirect,render,get_object_or_404
def course_list(request):
    courses=Course.objects.all()
    return render(request,'university/course/course_list.html',{'courses':courses})

def course_detail(request,course_id,dept_id):
    course = get_object_or_404(Course,course_id=course_id,dept_id=dept_id)
    return render(request, 'university/course/course_detail.html', {'course': course})

def course_create(reqest):
    if reqest.method=='POST':
        form=CourseForm(reqest.POST)
        if form.is_valid():
            form.save()
            return redirect('course-list')
    else:
        form=CourseForm()
    return render(reqest,'university/course/course_create.html',{'form':form})

def course_delete(request,course_id,dept_id):
    courses = get_object_or_404(Course,course_id=course_id,dept_id=dept_id)
    if request.method == 'POST':
        courses.delete()
        return redirect('course-list')
    return render(request, 'university/course/course_delete.html', {'courses': courses})

def course_update(request,course_id,dept_id):
    course = get_object_or_404(Course, course_id=course_id,dept_id=dept_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course-detail',course.course_id,course.dept_id)
    else:
        form = CourseForm(instance=course)
    return render(request, 'university/course/course_update.html', {'form': form})

