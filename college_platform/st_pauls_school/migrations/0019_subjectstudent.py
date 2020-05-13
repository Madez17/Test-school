# Generated by Django 3.0.6 on 2020-05-10 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('st_pauls_school', '0018_student_course_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='st_pauls_school.Student')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='st_pauls_school.Subject')),
            ],
        ),
    ]
