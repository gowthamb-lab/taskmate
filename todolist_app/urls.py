from todolist_app import views
from django.urls import path

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('about/', views.about, name =  'about'),
    path('contact-us/', views.contact, name = 'contact'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),  # New URL pattern
    path('pending/<int:task_id>/', views.pending_task, name='pending_task'),  # New URL pattern
]