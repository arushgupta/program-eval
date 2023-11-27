from django import forms
from university.models import Department, Faculty, Program

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'dept_code']

class AddFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'

class UpdateFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["uni_id"].disabled = True

class AddProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'
