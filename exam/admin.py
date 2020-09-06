from django.contrib import admin

from .models import (
    ExamQuestions,
    ExamAnswers,
)


admin.site.register(ExamQuestions),
admin.site.register(ExamAnswers)
