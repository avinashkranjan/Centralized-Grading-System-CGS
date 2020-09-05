from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    dept_code = models.CharField(max_length=5)
    year = models.IntegerField(max_length=4)
    roll_no = models.IntegerField(max_length=12)
    registration_no = models.IntegerField(max_length=20)
    mobile_no = models.IntegerField(max_length=10)


class Score(models.Model):
    roll_no = models.IntegerField(max_length=12)
    subject_code = models.CharField(max_length=6)
    credit_score = models.FloatField()

