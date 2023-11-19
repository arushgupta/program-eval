from django.db import models
from django.utils.translation import gettext_lazy as _

class Department(models.Model):
    name = models.CharField(_("Name"), max_length=50, unique=True)
    dept_code = models.CharField(_("Code"), max_length=4, unique=True)

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

class ProgramAdmin(models.Model):
    name = models.CharField(_("Admin Name"), max_length=255)
    uni_id = models.CharField(_("University ID"), max_length=9, unique=True)
    email = models.CharField(_("Email"), max_length=50)

    class Meta:
        verbose_name = _('Program Adminstrator')
        verbose_name = _('Program Administrators')

# TODO: Check for models.SET_NULL
class Program(models.Model):
    name = models.CharField(_("Name"), max_length=100, unique=True)
    admin = models.ForeignKey(_("Admin"), ProgramAdmin, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(_("Department"), Department, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('Program')
        verbose_name_plural = _('Programs')

# TODO: Check for models.SET_NULL
class Faculty(models.Model):
    class RankType(models.IntegerChoices):
        FULL = 1, _('Full')
        ASSOCIATE = 2, _('Associate')
        ASSISTANT = 3, _('Assistant')
        ADJUNCT = 4, _('Adjunct')

    name = models.CharField(_("Name"), max_length=50)
    uni_id = models.CharField(_("University ID"), max_length=9, unique=True)
    email = models.CharField(_("Email"), max_length=50)
    rank = models.PositiveSmallIntegerField(_("Rank"), choices=RankType.choices, default=RankType.ADJUNCT)
    department = models.ForeignKey(_("Department"), Department, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('Faculty')
        verbose_name_plural = _('Faculty Members')
