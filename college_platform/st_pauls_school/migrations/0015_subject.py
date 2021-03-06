# Generated by Django 3.0.6 on 2020-05-10 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st_pauls_school', '0014_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(default='', max_length=150, verbose_name='Subject Name')),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
                'ordering': ['subject_name'],
            },
        ),
    ]
