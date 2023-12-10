from django import forms
from university.generator import generate_unique_code
from university.models import Department, Faculty, Objective, Program, Course, ProgramCourse, ProgramCourseObjective, ProgramObjective, Section, SectionEvaluation, SubObjective

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
        self.fields["code"].required = False # Make the code field optional

    def clean_code(self):
        code = self.cleaned_data['code']

        # If the code is not entered by the user, generate one automatically
        if not code:
            code = generate_unique_code()
        return code

class UpdateObjectiveForm(forms.ModelForm):
    class Meta:
        model = Objective
        fields = ['code', 'title']
    
    def __init__(self, objective, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["code"].label = "Code"
        self.fields["code"].initial = objective.code
        self.fields["code"].disabled = True
        

class AddSubObjectiveForm(forms.ModelForm):
    class Meta:
        model = SubObjective
        fields = ['objective', 'description']
    
    def __init__(self, objective, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["objective"].label = "Objective"
        self.fields["objective"].initial = objective
        self.fields["objective"].disabled = True

class UpdateSubObjectiveForm(forms.ModelForm):
    class Meta:
        model = SubObjective
        fields = '__all__'
    
    def __init__(self, objective, sub_objective, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["objective"].label = "Objective"
        self.fields["objective"].disabled = True

class AddProgramObjectivesForm(forms.ModelForm):
    class Meta:
        model = ProgramObjective
        fields = '__all__'

    def __init__(self, program, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["program"].initial = program
        self.fields["program"].disabled = True

class AddProgramCourseObjectivesForm(forms.ModelForm):
    class Meta:
        model = ProgramCourseObjective
        fields = '__all__'
    
    def __init__(self, program, program_course, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["program_course"].initial = program_course
        self.fields["program_course"].disabled = True
        self.fields["program_course"].label = "Course"
        self.fields["program_objective"].label = "Objective"
        self.fields["sub_objective"].label = "Sub-Objective"
        self.fields["sub_objective"].queryset = SubObjective.objects.none()
        self.fields["sub_objective"].required = False

        if 'program_objective' in self.data:
            try:
                po_id = int(self.data.get('program_objective'))
                program_objective = ProgramObjective.objects.get(pk=po_id)
                self.fields['sub_objective'].queryset = SubObjective.objects.filter(objective_id=program_objective.objective_id)
            except (ValueError, TypeError):
                pass
    
    def clean(self, *args, **kwargs):
        pc = self.cleaned_data['program_course']
        po = self.cleaned_data['program_objective']
        so = self.cleaned_data['sub_objective']

        if so:
            if ProgramCourseObjective.objects.filter(program_course=pc, program_objective=po, sub_objective=so).exists():
                raise forms.ValidationError("This Sub-Objective is already assigned to this course.")
            elif ProgramCourseObjective.objects.filter(program_course=pc, program_objective=po, sub_objective=None).exists():
                raise forms.ValidationError("The Objective is aleady assigned to this course.")
        else:
            if ProgramCourseObjective.objects.filter(program_course=pc, program_objective=po, sub_objective=so).exists():
                raise forms.ValidationError("The Objective is already assigned to this course.")
        
        if SubObjective.objects.filter(objective_id=po.objective_id).count() == 0:
            self.cleaned_data['has_sub_objectives'] = False
        
        super().clean(*args, **kwargs)

class AddEvaluationForm(forms.ModelForm):
    class Meta:
        model = SectionEvaluation
        fields = '__all__'
        widgets = {
            'section_sub_objective': forms.HiddenInput(),
        }

    def clean(self, *args, **kwargs):
        super().clean(*args, **kwargs)
        sso = self.cleaned_data['section_sub_objective']
        qualified = self.cleaned_data['qualified']
        
        if qualified < 0:
            raise forms.ValidationError("Please enter a valid number of students.")
        if qualified > sso.section.enrolled:
            raise forms.ValidationError(f"This section only has {sso.section.enrolled} students, please provide a value within range.")

    def __init__(self, sso, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["section_sub_objective"].initial = sso
        self.fields["section_sub_objective"].disabled = True
        
class UpdateEvaluationForm(forms.ModelForm):
    class Meta:
        model = SectionEvaluation
        fields = '__all__'
        widgets = {
            'section_sub_objective': forms.HiddenInput(),
        }
    
    def clean(self, *args, **kwargs):
        super().clean(*args, **kwargs)
        sso = self.cleaned_data['section_sub_objective']
        qualified = self.cleaned_data['qualified']
        
        if qualified < 0:
            raise forms.ValidationError("Please enter a valid number of students.")
        if qualified > sso.section.enrolled:
            raise forms.ValidationError(f"This section only has {sso.section.enrolled} students, please provide a value within range.")

    def __init__(self, sso, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["section_sub_objective"].initial = sso
        self.fields["section_sub_objective"].disabled = True
