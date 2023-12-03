from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from university.models import ProgramCourse
from university.forms import ProgramCourseForm
def programcourse_list(request,program_id):
    programcourse = ProgramCourse.objects.filter(program_id=program_id)
    return render(request, 'university/ProgramCourse/programcourse_listm.html', {'programcourse': programcourse,'program':program_id})

def programcourse_create(request,program_id):
    if request.method=='POST':
        form=ProgramCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('programcourse-list',program_id=program_id)
    else:
        form=ProgramCourseForm()
    return render(request,'university/ProgramCourse/programcourse_create.html',{'form':form,'program':program_id})

def programcourse_delete(request,program_id,course_id):
    programcourse=get_object_or_404(ProgramCourse,program_id=program_id,course_id=course_id)
    if request.method=='POST':
        programcourse.delete()
        return redirect('programcourse-list',program_id=program_id)
    return render(request,'university/programcourse/programcourse_delete.html',{'programcourse':programcourse , 'program':program_id})

