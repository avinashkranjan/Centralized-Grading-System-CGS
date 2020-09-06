from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(max_length=100)


# class Subject(models.Model):
#     name = models.CharField(max_length=30)
#     level = models.CharField(max_length=30, null=False)

#     def __str__(self):
#         return self.name
    

class Assignment(models.Model):

    def user_directory_path(instance, filename):
        return 'user_{0}/{1}'.format(instance.owner.id, filename)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    subject = models.ForeignKey('class.Class', on_delete=models.CASCADE)
    submission_date = models.DateField("Submission Date")
    date_added = models.DateField(auto_now_add=True)
    question = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.PositiveIntegerField(unique=True, null=False)
    sem = models.PositiveIntegerField(verbose_name="Semister", default=5)

    def __str__(self):
        return self.user.username
    

class StudentAnswer(models.Model):

    def user_directory_path(instance, filename):
        return 'user_{0}/{1}'.format(instance.student.id, filename)
        
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='assignment_answers')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    question = models.FileField(upload_to=user_directory_path)
    submitted_date = models.DateField(auto_now_add=True, null= True)


class AnswerRemark(models.Model):
    Remarks = models.TextField('Remarks', default="No remarks added!", null=True)
    studentanswer = models.ForeignKey(StudentAnswer, on_delete=models.CASCADE)

    def __str__(self):
        return self.Remarks


