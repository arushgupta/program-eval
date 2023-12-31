from django.urls import path
import university.views as views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Department
    path('departments/', views.department_list, name='dept-list'),
    path('departments/add/', views.department_create, name='dept-add'),
    path('departments/<str:pk>/', views.department_detail, name='dept-detail'),
    path('departments/<str:pk>/change/', views.department_update, name='dept-update'),
    path('departments/<str:pk>/remove/', views.department_delete, name='dept-delete'),
    path('departments/faculty/<str:pk>/re-hire/', views.department_rehire, name='department-rehire'),

    # Faculty
    path('faculty/', views.faculty_list, name='faculty-list'),
    path('faculty/add/', views.faculty_create, name='faculty-add'),
    path('faculty/<str:pk>/', views.faculty_detail, name='faculty-detail'),
    path('faculty/<str:pk>/change/', views.faculty_update, name='update-faculty'),
    path('faculty/<str:pk>/fire/', views.faculty_fire, name='fire-faculty'),
    
    # Program
    path('programs/', views.program_list, name='program-list'),
    path('programs/add/', views.program_create, name='program-add'),
    path('programs/<str:pk>/', views.program_detail, name='program-detail'),
    path('programs/<str:pk>/change/', views.program_update, name='program-update'),
    path('programs/<str:pk>/remove/', views.program_delete, name='program-delete'),
    
    # Add/Remove Courses from Programs
    path('programs/<str:program_id>/courses/add/', views.add_courses, name='program_course-add'),
    path('programs/<str:program_id>/courses/<str:course_id>/remove/', views.remove_courses, name='program_course-delete'),

    # Add/Remove (Sub)objectives from Program-Course
    path('programs/<str:program_id>/courses/<str:course_id>/objectives/add/', views.add_program_course_objective, name='program_course_obj-add'),
    path('programs/<str:program_id>/courses/<str:course_id>/objectives/<str:objective>/remove/', views.delete_program_course_objective, name='program_course_obj-delete'),

    # Add/Remove Objectives from Programs
    path('programs/<str:program_id>/objectives/add/', views.add_program_objective, name='program_obj-add'),
    path('ajax/load-sub-objectives/', views.load_sub_objectives, name='ajax-load-sub_objectives'),
    path('programs/<str:program_id>/objectives/<str:objective_id>/remove/', views.remove_program_objective, name='program_obj-delete'),
    
    # Section - Evaluations
    path('programs/<str:program_id>/courses/<str:course_id>/<int:semester>/<int:year>/<str:section_code>/', views.program_course_section_detail, name='program_course_section-detail'),
    path('programs/<str:program_id>/courses/<str:course_id>/<int:semester>/<int:year>/<str:section_code>/<int:sso_id>/add/', views.add_evaluation, name='evaluation-add'),
    path('programs/<str:program_id>/courses/<str:course_id>/<int:semester>/<int:year>/<str:section_code>/<int:sso_id>/update/', views.edit_evaluation, name='evaluation-update'),
    path('programs/<str:program_id>/courses/<str:course_id>/<int:semester>/<int:year>/<str:section_code>/<int:sso_id>/delete/', views.delete_evaluation, name='evaluation-delete'),
    
    # Course
    path('courses/', views.course_list, name='course-list'),
    path('courses/add/', views.course_create, name='course-add'),
    path('courses/<str:dept_id>/<str:course_id>/', views.course_detail, name='course-detail'),
    path('courses/<str:dept_id>/<str:course_id>/change/', views.course_update, name='course-update'),
    path('courses/<str:dept_id>/<str:course_id>/remove/', views.course_delete, name='course-delete'),
    
    # Add/Update/Delete Section
    path('courses/<str:dept_id>/<str:course_id>/sections/add/', views.add_section, name='section-add'),
    path('courses/<str:dept_id>/<str:course_id>/<str:code>/<str:semester>/<int:year>/change/', views.update_section, name='section-update'),
    path('courses/<str:dept_id>/<str:course_id>/<str:code>/<str:semester>/<int:year>/remove/', views.remove_section, name='section-delete'),

    # Objectives
    path('objectives/', views.objective_list, name='objective-list'),
    path('objectives/add/', views.objective_create, name='objective-add'),
    path('objectives/<str:code>/', views.objective_detail, name='objective-detail'),
    path('objectives/<str:code>/change/', views.objective_update, name='objective-update'),
    path('objectives/<str:code>/remove/', views.objective_delete, name='objective-delete'),

    # Sub-Objectives
    path('objectives/<str:code>/sub/add/', views.add_sub_objective, name='sub_objective-add'),
    path('objectives/<str:o_code>/<str:s_code>/change/', views.update_sub_objective, name='sub_objective-update'),
    path('objectives/<str:o_code>/<str:s_code>/remove/', views.delete_sub_objective, name='sub_objective-delete'),

    # Evaluation Results
    path('semester-evaluations/', views.get_semester_program_evaluation, name='get-semester-program-evaluation'),
    path('yearly-evaluations/', views.get_yearly_evaluation, name='get-yearly-evaluation'),
]
