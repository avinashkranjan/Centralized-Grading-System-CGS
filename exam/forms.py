from django import forms
from .models import (
    ExamQuestions,
    ExamAnswers
)



class ExamQuestionAddForm(forms.ModelForm):
    class Meta:
        model = ExamQuestions
        fields = ['subject', 'exam_date', 'question1', 'question1_total_marks', 'question2', 'question2_total_marks', 'question3', 'question3_total_marks', 'full_marks']


class ExamAnswerAddForm(forms.ModelForm):
    class Meta:
        model = ExamAnswers
        fields = ['question1_answer', 'question2_answer', 'question3_answer']

class ExamAnswerCheckForm(forms.ModelForm):
    class Meta:
        model = ExamAnswers
        fields = ['question1_marks', 'question2_marks', 'question3_marks']