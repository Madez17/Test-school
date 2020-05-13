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
                print('Si es correcto')
                return email
            else:
                print('Este no es su email registrado')



                
        # print(Teacher.objects.filter(email='maf@gma.com'))
        # if email == Teacher.objects.filter(email='maf@gma.com'):
        #     print('EsTE CORREO EXISTE')

    # def clean_password(self):
    #     email = self.cleaned_data.get('password')
    #     password = cleaned_data.get("password")
    #     if password != password:
    #         print('Esta no es su password')
    #         raise forms.ValidationError(
    #             "password and confirm_password does not match"
    #         )
    #     else:
    #         print('esto es correcto password')