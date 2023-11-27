from django.urls import path, re_path
import university.views as views

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
]
