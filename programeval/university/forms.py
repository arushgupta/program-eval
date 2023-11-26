from django import forms
from django.core.validators import EmailValidator, validate_email
from django.core.exceptions import ValidationError
from university.models import Department, Faculty

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
