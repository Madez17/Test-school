# Generated by Django 3.0.6 on 2020-05-10 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st_pauls_school', '0023_subjectstudentscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='scores',
            field=models.ManyToManyField(through='st_pauls_school.SubjectStudentScore', to='st_pauls_school.Subject'),
        ),
    ]
