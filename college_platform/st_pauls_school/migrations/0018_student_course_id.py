# Generated by Django 3.0.6 on 2020-05-10 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('st_pauls_school', '0017_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='st_pauls_school.Course'),
        ),
    ]