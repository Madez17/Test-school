from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key = True)
    course_name = models.CharField('Course Name', max_length = 150, blank = False, null = False)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['course_name']
    
    def __str__(self):
        return self.course_name

class Subject(models.Model):
    id = models.AutoField(primary_key = True)
    subject_name = models.CharField('Subject Name', default="", max_length = 150, blank = False, null = False)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'
        ordering = ['subject_name']
    
    def __str__(self):
        return self.subject_name

class Teacher(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Name', max_length = 200, blank = False, null = False)
    last_name = models.CharField('Last Name', max_length = 200, blank = False, null = False)
    email = models.EmailField('Email', max_length = 200, blank = False, null = False)
    password = models.CharField('password', max_length = 200, blank = False, null = False)
    course_id = models.OneToOneField(Course, on_delete = models.CASCADE)
    subject_id = models.OneToOneField(Subject, on_delete = models.CASCADE)
    # objects = models.Manager()

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ['name']

    def __str__(self):
        return self.name

class Student(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Name', max_length = 200, blank = False, null = False)
    last_name = models.CharField('Last Name', max_length = 200, blank = False, null = False)
    email = models.EmailField('Email', max_length = 200, blank = False, null = False)
    password = models.CharField('password', max_length = 200, blank = False, null = False)
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE, default = "")
    subjects = models.ManyToManyField(Subject, through = 'SubjectStudent')

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['name']

    def __str__(self):
        return self.name


class SubjectStudent(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete = models.CASCADE)
    

    class Meta:
        verbose_name = 'SubjectStudent'
        verbose_name_plural = 'SubjectStudent'
        ordering = ['student_id']

    def __str__(self):
        return '{} / {}'.format(self.student_id, self.subject_id)

class Score(models.Model):
    id = models.AutoField(primary_key = True)
    score = models.IntegerField('Score', blank = False, null = False)
    scores = models.ManyToManyField(Subject, through = 'SubjectStudentScore')

    class Meta:
        verbose_name = 'Score'
        verbose_name_plural = 'Scores'
        ordering = ['score']
    
    def __str__(self):
        return '{}'.format(self.score)


class SubjectStudentScore(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete = models.CASCADE)
    score_id = models.ForeignKey(Score, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'SubjectStudentScore'
        verbose_name_plural = 'SubjectStudentScores'
        ordering = ['student_id']

    def __str__(self):
        return '{} / {} / {}'.format(self.student_id, self.subject_id, self.score_id)


