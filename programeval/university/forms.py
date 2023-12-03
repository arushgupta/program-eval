from django import forms
from university.models import Department, Faculty, Program,Course,ProgramCourse

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'dept_code']

class AddFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        exclude = ('is_active', )

class UpdateFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        exclude = ('is_active', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["uni_id"].disabled = True

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.admin = Faculty.objects.filter(is_active=True).order_by('uni_id')
        super().__init__(*args, **kwargs)
        self.fields["admin"].queryset = self.admin

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=['course_id','dept','title','description']

class ProgramCourseForm(forms.ModelForm):
    class Meta:
        model=ProgramCourse
        fields=['course','program']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["program"].disabled = True
        # self.fields["course"].queryset = ProgramCourse.objects.filter(program_id=program_id)

