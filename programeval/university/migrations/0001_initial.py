# Generated by Django 4.2.7 on 2023-12-06 03:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Course ID')),
                ('title', models.CharField(max_length=50, verbose_name='Course Title')),
                ('description', models.TextField(verbose_name='Course Description')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('dept_code', models.CharField(max_length=4, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Code')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('uni_id', models.CharField(max_length=4, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='University ID')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('rank', models.PositiveSmallIntegerField(choices=[(1, 'Full'), (2, 'Associate'), (3, 'Assistant'), (4, 'Adjunct')], default=4, verbose_name='Rank')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_dept', to='university.department')),
            ],
            options={
                'verbose_name': 'Faculty',
                'verbose_name_plural': 'Faculty Members',
            },
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Objective Code')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Objective',
                'verbose_name_plural': 'Objectives',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='Name')),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prog_admin', to='university.faculty')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prog_dept', to='university.department')),
            ],
            options={
                'verbose_name': 'Program',
                'verbose_name_plural': 'Programs',
            },
        ),
        migrations.CreateModel(
            name='ProgramCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='university.course')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program', to='university.program')),
            ],
            options={
                'unique_together': {('course', 'program')},
            },
        ),
        migrations.CreateModel(
            name='ProgramCourseObjective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation_method', models.CharField(max_length=50, verbose_name='Evaluation Method')),
                ('objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program_courses', to='university.objective')),
                ('program_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objectives', to='university.programcourse')),
            ],
            options={
                'verbose_name': 'Program Course Objective',
                'verbose_name_plural': 'Program Course Objectives',
                'unique_together': {('program_course', 'objective')},
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Section ID')),
                ('semester', models.PositiveSmallIntegerField(choices=[(1, 'Spring'), (2, 'Summer'), (3, 'Fall')], default=3, verbose_name='Semester')),
                ('year', models.PositiveSmallIntegerField(choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027)], default=2023, verbose_name='Year')),
                ('enrolled', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Enrolled Students')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_course', to='university.course')),
                ('prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_prof', to='university.faculty')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
                'unique_together': {('code', 'course', 'semester', 'year')},
            },
        ),
        migrations.AddField(
            model_name='course',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_dept', to='university.department'),
        ),
        migrations.CreateModel(
            name='SubObjective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Description')),
                ('objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='so_objectives', to='university.objective')),
            ],
            options={
                'verbose_name': 'Sub-Objective',
                'verbose_name_plural': 'Sub-Objectives',
                'unique_together': {('id', 'objective')},
            },
        ),
        migrations.CreateModel(
            name='SectionObjectiveEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students_met', models.PositiveIntegerField(default=0, verbose_name='Number of Students Met')),
                ('program_course_objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_evaluations', to='university.programcourseobjective')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objective_evaluations', to='university.section')),
            ],
            options={
                'verbose_name': 'Section Objective Evaluation',
                'verbose_name_plural': 'Section Objective Evaluations',
                'unique_together': {('section', 'program_course_objective')},
            },
        ),
        migrations.CreateModel(
            name='ProgramObjective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='po_objective', to='university.objective')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='po_program', to='university.program')),
            ],
            options={
                'verbose_name': 'Program Objective',
                'verbose_name_plural': 'Program Objectives',
                'unique_together': {('program', 'objective')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('course_id', 'dept')},
        ),
    ]
