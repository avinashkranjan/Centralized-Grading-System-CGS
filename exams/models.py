from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    dept_code = models.CharField(max_length=5)
    year = models.IntegerField()
    roll_no = models.IntegerField(primary_key=True)
    registration_no = models.IntegerField()
    mobile_no = models.IntegerField()


class Score(models.Model):
    roll_no = models.IntegerField()
    subject_code = models.CharField(max_length=6)
    credit_score = models.FloatField()

