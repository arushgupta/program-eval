from django import forms
from university.models import Department, Faculty, Objective, Program, Course, ProgramCourse, Section

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'dept_code']

class UpdateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dept_code', 'name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["dept_code"].disabled = True

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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["dept"].label = "Department"

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

class AddSectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['course', 'code', 'semester', 'year', 'prof', 'enrolled']

    def __init__(self, department, course, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["course"].initial = Course.objects.get(course_id=course, dept_id=department)
        self.fields["course"].disabled = True
        self.fields["prof"].queryset = Faculty.objects.filter(is_active=True)
        self.fields["prof"].label = "Professor"

class UpdateSectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['course', 'code', 'semester', 'year', 'prof', 'enrolled']
    
    def __init__(self, department, course, section, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["course"].initial = course
        self.fields["course"].disabled = True
        self.fields["prof"].queryset = Faculty.objects.filter(is_active=True)
        self.fields["prof"].label = "Professor"

class AddObjectiveForm(forms.ModelForm):
    class Meta:
        model = Objective
        fields = ['title', 'code']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["code"].label = "Code"

class UpdateObjectiveForm(forms.ModelForm):
    class Meta:
        model = Objective
        fields = ['title']
