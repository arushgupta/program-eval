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
    path('faculty/<str:pk>/change/', views.faculty_update, name='faculty-update'),
    path('faculty/<str:pk>/fire/', views.faculty_fire, name='faculty-fire'),
]
