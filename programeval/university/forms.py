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

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['dept','course_id','title','description']

class UpdateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['dept','course_id','title','description']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["dept"].disabled = True

class ProgramCourseForm(forms.ModelForm):
    class Meta:
        model = ProgramCourse
        fields = ['program', 'course']
        
    def __init__(self, department, program, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["program"].initial = program
        self.fields["program"].disabled = True
        self.fields["course"].queryset = Course.objects.filter(dept=department)

