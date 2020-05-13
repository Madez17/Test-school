from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import Teacher, Student
from .forms import TeacherForm
from django.views import generic

def index(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('st_pauls_school/teacher')
        else:
            form = TeacherForm()
    return render(request, 'st_pauls_school/index.html', {'form': form})

def Teacher(request):
    # test = models.Teacher.objects.get(name='Mafe')
    # return render(request, 'st_pauls_school/teacher.html', {'test': test})
    return render(request, 'st_pauls_school/teacher.html')

def Student(request):
    return render(request, 'st_pauls_school/student.html')

# def createTeacher(request):
#     if request.method == 'POST':
#         teacher_form = TeacherForm(request.POST)
#         if teacher_form.is_valid():
#             teacher_form.save()
#             return redirect('index')
#     else:
#         teacher_form = TeacherForm()
#     return render(request, 'st_pauls_school/create_teacher.html', {'teacher_form':teacher_form})
