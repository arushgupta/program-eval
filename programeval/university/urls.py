from django.urls import path, re_path
from university import views

urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.department_list, name='dept-list'),
    path('departments/add/', views.department_create, name='dept-add'),
    path('departments/<str:pk>/', views.department_detail, name='dept-detail'),
    path('departments/<str:pk>/change/', views.department_update, name='dept-update'),
    path('departments/<str:pk>/remove/', views.department_delete, name='dept-delete'),
]
