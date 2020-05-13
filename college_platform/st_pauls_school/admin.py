from django.contrib import admin

# Register your models here.
from .models import Course, Subject, Teacher, Student, SubjectStudent, Score, SubjectStudentScore

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(SubjectStudent)
admin.site.register(Score)
admin.site.register(SubjectStudentScore)