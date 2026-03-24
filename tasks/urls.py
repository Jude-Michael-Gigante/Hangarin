from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_add, name='category_add'),
    path('categories/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),
    path('priorities/', views.priority_list, name='priority_list'),
    path('priorities/add/', views.priority_add, name='priority_add'),
    path('priorities/edit/<int:pk>/', views.priority_edit, name='priority_edit'),
    path('priorities/delete/<int:pk>/', views.priority_delete, name='priority_delete'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.task_add, name='task_add'),
    path('tasks/edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('tasks/delete/<int:pk>/', views.task_delete, name='task_delete'),
]