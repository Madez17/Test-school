# Generated by Django 3.0.6 on 2020-05-08 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st_pauls_school', '0004_auto_20200508_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=150, verbose_name='Course Name'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(max_length=150, verbose_name='Subject Name'),
        ),
    ]