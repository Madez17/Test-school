# Generated by Django 3.0.6 on 2020-05-08 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st_pauls_school', '0002_auto_20200508_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=200, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='password',
            field=models.CharField(max_length=200, verbose_name='password'),
        ),
    ]
