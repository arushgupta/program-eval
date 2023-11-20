from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator, MinValueValidator

class Department(models.Model):
    name = models.CharField(_("Name"), max_length=50, unique=True)
    dept_code = models.CharField(_("Code"), max_length=4, unique=True, primary_key=True, validators=[MinLengthValidator(1)])

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
    uni_id = models.CharField(_("University ID"), max_length=9, unique=True, primary_key=True)
    email = models.CharField(_("Email"), max_length=50)
    rank = models.PositiveSmallIntegerField(_("Rank"), choices=RankType.choices, default=RankType.ADJUNCT)
    department = models.ForeignKey(_("Department"), Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Faculty')
        verbose_name_plural = _('Faculty Members')

class Program(models.Model):
    name = models.CharField(_("Name"), max_length=100, unique=True, primary_key=True)
    admin = models.ForeignKey(_("Admin"), Faculty, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(_("Department"), Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Program')
        verbose_name_plural = _('Programs')

class Course(models.Model):
    course_id = models.CharField(_('Course ID'), max_length=4, validators=[MinLengthValidator(4)])
    dept = models.ForeignKey(_('Department'), Department, on_delete=models.CASCADE)
    title = models.CharField(_('Course Title'), max_length=50)
    description = models.TextField(_('Course Description'))

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')
        unique_together = ('course_id', 'dept')

# Junction Table to allow for many-to-many relation between Course and Program
class ProgramCourse(models.Model):
    course = models.ForeignKey(_('Course'), Course, on_delete=models.CASCADE)
    program = models.ForeignKey(_('Program'), Program, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('course', 'program')

class Section(models.Model):
    class Semester(models.IntegerChoices):
        FALL = 1, _('Fall')
        SPRING = 2, _('Spring')
        SUMMER = 3, _('Summer')

    section_id = models.CharField(_('Section ID'), max_length=3, validators=[MinLengthValidator(3)])
    semester = models.PositiveSmallIntegerField(_('Semester'), choices=Semester.choices, default=Semester.FALL)
    year = models.CharField(_('Year'), max_length=4, validators=[MinLengthValidator(4)])
    prof = models.ForeignKey(_('Professor'), Faculty, on_delete=models.SET_NULL)
    course = models.ForeignKey(_('Course'), Course, on_delete=models.CASCADE)
    enrolled = models.PositiveIntegerField(_('Enrolled Students'), default=0, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')
        unique_together = ('section_id', 'course')

class LearningObjective(models.Model):
    code = models.CharField(_("LO code"), max_length=10, validators=[MinLengthValidator(3)], unique=True)
    title = models.CharField(_("Title"), max_length=50)

class SubObjective(models.Model):
    code = models.IntegerField(_("SO Code"))
    description = models.TextField(_("SO Description"))
    lo = models.ForeignKey(_("Learning Objective"), LearningObjective, on_delete=models.CASCADE)

class ProgramCourseObjective(models.Model):
    programcourse = models.ForeignKey(_('Program Course Pair'), ProgramCourse, on_delete=models.CASCADE)
    objective = models.ForeignKey(_('Objective'), SubObjective, on_delete=models.CASCADE)

# TODO: Create a table that links Section and Subobjective
# class Evaluation(models.Model):
#     section
#     SubObjective
#     evalution_type
#     student_count
