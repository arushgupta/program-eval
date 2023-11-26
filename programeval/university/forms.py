from django import forms
from university.models import Department, Faculty

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'dept_code']

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'
