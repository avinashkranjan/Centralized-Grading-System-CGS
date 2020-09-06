from django.db import models

from assignment.models import (
    User,
    Student,
)


class ExamQuestions(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    subject = models.ForeignKey('class.Class', on_delete=models.CASCADE)
    exam_date = models.DateField("Submission Date")

    question1 = models.TextField('Question 1', default="Add Question", null=True)
    question1_total_marks = models.PositiveIntegerField(null=False, default=1)

    question2 = models.TextField('Question 2', default="Add Question", null=True)
    question2_total_marks = models.PositiveIntegerField(null=False, default=1)

    question3 = models.TextField('Question 3', default="Add Question", null=True)
    question3_total_marks = models.PositiveIntegerField(null=False, default=1)

    full_marks = models.PositiveIntegerField()

    def __str__(self):
        return str(self.owner.username + "-" + self.subject.class_name)


class ExamAnswers(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='exam_answer')
    examQuestions = models.ForeignKey(ExamQuestions, on_delete=models.CASCADE)

    question1_answer = models.TextField('Question 1 Answer', default="Your Answer", null=True)
    question1_marks = models.PositiveIntegerField(null=True)

    question2_answer = models.TextField('Question 2 Answer', default="Your Answer", null=True)
    question2_marks = models.PositiveIntegerField(null=True)

    question3_answer = models.TextField('Question 3 Answer', default="Your Answer", null=True)
    question3_marks = models.PositiveIntegerField(null=True)

    total_marks_obtained = models.PositiveIntegerField(null=True)

    def __str__(self):
        return(self.examQuestions.subject.class_name + '-' + self.student.user.username)

