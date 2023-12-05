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
    
    # Course
    path('courses/', views.course_list, name='course-list'),
    path('courses/add/', views.course_create, name='course-add'),
    path('courses/<str:dept_id>/<str:course_id>/', views.course_detail, name='course-detail'),
    path('courses/<str:dept_id>/<str:course_id>/change/', views.course_update, name='course-update'),
    path('courses/<str:dept_id>/<str:course_id>/remove/', views.course_delete, name='course-delete'),
    
    # Add/Update/Delete Section
    path('courses/<str:dept_id>/<str:course_id>/sections/add', views.add_section, name='section-add'),
    path('courses/<str:dept_id>/<str:course_id>/<str:section_id>/change/', views.update_section, name='section-update'),
    path('courses/<str:dept_id>/<str:course_id>/<str:section_id>/remove', views.remove_section, name='section-delete'),
    path('objectives/', views.objective_list, name='objective-list'),
    path('objectives/<str:pk>/', views.objective_detail, name='objective-detail'),
    path('objectives/add/', views.objective_create, name='objective-add'),
    path('objectives/<str:pk>/update/', views.objective_update, name='objective-update'),
    path('objectives/<str:pk>/delete/', views.objective_delete, name='objective-delete'),
    path('courses/<str:course_id>/assign-objective/', views.assign_objective_to_course, name='assign-objective-to-course')
]
