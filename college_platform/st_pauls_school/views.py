from django.db import models
from django.shortcuts import render, redirect
from .models import Teacher, Student
from .forms import TeacherForm, StudentForm

#Home
def index(request):
    return render(request, 'st_pauls_school/index.html')
    
# Teacher Login
def Teachers(request):
    form = TeacherForm(request.POST or None)
    # user_email = request.POST['email']

    # user_email = request.POST.get("email")
    # test = Teacher.objects.filter(email=user_email)
    # print(test)
    
    if form.is_valid():
        return redirect('dashboard/')
    return render(request, 'st_pauls_school/teacher.html', {'form': form})


# Teacher Dasboard view
def TeacherDasboard(request):
    test = Teacher.objects.all()
    return render(request, 'st_pauls_school/tdashboard.html', {'test': test})


# Student Login
def Students(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        return redirect('dashboard/')
    return render(request, 'st_pauls_school/student.html', {'form': form})

# Student Dasboard view
def StudentDasboard(request):
    test = Student.objects.all()
    return render(request, 'st_pauls_school/sdashboard.html', {'test': test})