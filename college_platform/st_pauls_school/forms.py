from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Teacher, Student, Course, Subject, Score


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['email', 'password']
        widgets = {
            'email' : forms.TextInput(attrs={'placeholder' : 'Email', 'name' : "email"}),
            'password' : forms.PasswordInput(attrs={'placeholder' : 'password', 'name': 'password'})
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        for instance in Teacher.objects.all():
            if instance.email == email:
                return email
        raise forms.ValidationError('This user is not register' + email)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        for instance in Teacher.objects.all():
            if instance.password == password:
                return password
        raise forms.ValidationError('Wrong Password')



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['email', 'password']
        widgets = {
            'email' : forms.TextInput(attrs={'placeholder' : 'Email', 'name' : "email"}),
            'password' : forms.PasswordInput(attrs={'placeholder' : 'password', 'name': 'password'})
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        for instance in Student.objects.all():
            if instance.email == email:
                return email
        raise forms.ValidationError('This user is not register' + email)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        for instance in Student.objects.all():
            if instance.password == password:
                return password
        raise forms.ValidationError('Wrong Password')