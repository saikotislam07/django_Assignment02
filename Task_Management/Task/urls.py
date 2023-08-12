from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_task, name='show_task'),
    path('store_task/', views.store_task, name='store_task'),
    path('edit_task/<str:Title>/', views.edit_task, name='edit_task'),
    path('delete_task/<str:Title>/', views.delete_task, name='delete_task'),
    path('complete_task/<str:Title>/', views.complete_task, name='complete_task'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
]

