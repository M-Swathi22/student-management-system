from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'), 
    path('add/', views.add_student, name='add_student'),
    path('view/', views.view_students, name='view_students'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('student-login/', views.student_login, name='student_login'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),

]

# Create your views here.
