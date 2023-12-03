from django.urls import path, re_path
import university.views as views
# from university.views import course_views
urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.department_list, name='dept-list'),
    path('departments/add/', views.department_create, name='dept-add'),
    path('departments/<str:pk>/', views.department_detail, name='dept-detail'),
    path('departments/<str:pk>/change/', views.department_update, name='dept-update'),
    path('departments/<str:pk>/remove/', views.department_delete, name='dept-delete'),
    path('faculty/', views.faculty_list, name='faculty-list'),
    path('faculty/add/', views.faculty_create, name='faculty-add'),
    path('faculty/<str:pk>/', views.faculty_detail, name='faculty-detail'),
    path('faculty/<str:pk>/change/', views.faculty_update, name='update-faculty'),
    path('faculty/<str:pk>/fire/', views.faculty_fire, name='fire-faculty'),
    path('programs/', views.program_list, name='program-list'),
    path('programs/add/', views.program_create, name='program-add'),
    path('programs/<str:pk>/', views.program_detail, name='program-detail'),
    path('programs/<str:pk>/change/', views.program_update, name='program-update'),
    path('programs/<str:pk>/remove/', views.program_delete, name='program-delete'),
    path('courses/',views.course_list,name='course-list'),
    path('courses/add/',views.course_create,name='course-add'),
    path('courses/<str:course_id>/<str:dept_id>/',views.course_detail,name='course-detail'),
    path('courses/<str:course_id>/<str:dept_id>/change/', views.course_update, name='course-update'),
    path('courses/<str:course_id>/<str:dept_id>/remove/', views.course_delete, name='course-delete'),
    path('programs/<str:program_id>/courses/',views.programcourse_list,name='programcourse-list'),
    path('programs/<str:program_id>/courses/add/',views.programcourse_create,name='programcourse-add'),
    # path('programs/<str:program_id>/courses/<str:course_id>/change/',views.programcourse_update,name='programcourse-update'),
    path('programs/<str:program_id>/courses/<str:course_id>/remove/',views.programcourse_delete,name='programcourse-delete'),
    
]
