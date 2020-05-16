from django.urls import path
from . import views

app_name = 'st_pauls_school'
urlpatterns = [
    path('', views.index, name='index'),
    path('teacher/', views.Teachers, name = 'teacher'),
    path('teacher/dashboard/', views.TeacherDasboard, name = 'teacherdashboard'),
    path('student/', views.Students, name = 'student'),
    path('student/dashboard/', views.StudentDasboard, name = 'studentdashboard'),
]

