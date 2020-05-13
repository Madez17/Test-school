from django.urls import path
from . import views

app_name = 'st_pauls_school'
urlpatterns = [
    path('', views.index, name='index'),
    path('teacher/', views.Teacher, name = 'teacher'),
    path('student/', views.Student, name = 'student')
]

