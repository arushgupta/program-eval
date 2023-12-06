from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator, MinValueValidator
from datetime import datetime

class Department(models.Model):
    name = models.CharField(_("Name"), max_length=50, unique=True)
    dept_code = models.CharField(_("Code"), max_length=4, unique=True, primary_key=True, validators=[MinLengthValidator(1)])

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

class Faculty(models.Model):
    class RankType(models.IntegerChoices):
        FULL = 1, _('Full')
        ASSOCIATE = 2, _('Associate')
        ASSISTANT = 3, _('Assistant')
        ADJUNCT = 4, _('Adjunct')

    name = models.CharField(_("Name"), max_length=50)
    uni_id = models.CharField(_("University ID"), max_length=4, unique=True, primary_key=True, validators=[MinLengthValidator(4)])
    email = models.EmailField(_("Email"), max_length=50, blank=False)
    rank = models.PositiveSmallIntegerField(_("Rank"), choices=RankType.choices, default=RankType.ADJUNCT)
    department = models.ForeignKey(Department, related_name='faculty_dept', on_delete=models.CASCADE)
    is_active = models.BooleanField(_("Is Active"), default=True)

    def __str__(self):
        return f"{self.uni_id}: {self.name}"

    class Meta:
        verbose_name = _('Faculty')
        verbose_name_plural = _('Faculty Members')


class Program(models.Model):
    name = models.CharField(_("Name"), max_length=100, unique=True, primary_key=True)
    admin = models.ForeignKey(Faculty, on_delete=models.SET_NULL, related_name='prog_admin',null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='prog_dept')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _('Program')
        verbose_name_plural = _('Programs')

class Course(models.Model):
    course_id = models.CharField(_('Course ID'), max_length=4, validators=[MinLengthValidator(4)])
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='course_dept')
    title = models.CharField(_('Course Title'), max_length=50)
    description = models.TextField(_('Course Description'))

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')
        unique_together = ('course_id', 'dept')

    def __str__(self):
        return f"{self.dept.dept_code}{self.course_id}"

# Junction Table to allow for many-to-many relation between Course and Program
class ProgramCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='program')
    
    class Meta:
        unique_together = ('course', 'program')

class Section(models.Model):
    class Semester(models.IntegerChoices):
        SPRING = 1, _('Spring')
        SUMMER = 2, _('Summer')
        FALL = 3, _('Fall')

    years = []
    for y in range(2010, (datetime.now().year + 5)):
        years.append((y, y))

    code = models.CharField(_('Section ID'), max_length=3, validators=[MinLengthValidator(3)])
    semester = models.PositiveSmallIntegerField(_('Semester'), choices=Semester.choices, default=Semester.FALL)
    year = models.PositiveSmallIntegerField(_('Year'), choices=years, default=datetime.now().year)
    prof = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='section_prof')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='section_course')
    enrolled = models.PositiveIntegerField(_('Enrolled Students'), default=0, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')
        unique_together = ('code', 'course', 'semester', 'year')


class Objective(models.Model):
    code = models.CharField(_("Objective Code"), max_length=5, validators=[MinLengthValidator(3)], primary_key=True)
    title = models.CharField(_("Title"), max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Objective')
        verbose_name_plural = _('Objectives')

class SubObjective(models.Model):
    code = models.CharField(_("Sub-Objective Code"), max_length=5, validators=[MinLengthValidator(3)], primary_key=True)
    description = models.TextField(_("Description"))
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE, related_name='so_objectives')

    def __str__(self):
        return f"{self.objective.code} - {self.code}"
    
    class Meta:
        verbose_name = _('Sub-Objective')
        verbose_name_plural = _('Sub-Objectives')
        unique_together = ('code', 'objective')

class ProgramCourseObjective(models.Model):
    program_course = models.ForeignKey(ProgramCourse, on_delete=models.CASCADE, related_name='objectives')
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE, related_name='program_courses')
    evaluation_method = models.CharField(_("Evaluation Method"), max_length=50)

    def __str__(self):
        return f"{self.program_course} - {self.objective}"

    class Meta:
        verbose_name = _("Program Course Objective")
        verbose_name_plural = _("Program Course Objectives")
        unique_together = ('program_course', 'objective')

class SectionObjectiveEvaluation(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='objective_evaluations')
    program_course_objective = models.ForeignKey(ProgramCourseObjective, on_delete=models.CASCADE, related_name='section_evaluations')
    students_met = models.PositiveIntegerField(_("Number of Students Met"), default=0)

    def __str__(self):
        return f"{self.section} - {self.program_course_objective}"

    class Meta:
        verbose_name = _("Section Objective Evaluation")
        verbose_name_plural = _("Section Objective Evaluations")
        unique_together = ('section', 'program_course_objective')

# TODO: Create a table that links Section and Subobjective
# class Evaluation(models.Model):
#     section
#     SubObjective
#     evalution_type
#     student_count
