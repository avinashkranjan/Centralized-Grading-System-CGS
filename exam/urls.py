from django.urls import path, include
from .views import (
    exam_view,
    exam_home,
    exam_add,
    exam_update,
    exam_delete,
    exam_answer_list,
    exam_answer_check,

    student_exam_home,
    exam_submit,
)

urlpatterns = [
    path('', exam_view, name="exam_page"),

    path('teachers/', exam_home, name='exam_page_details_teacher'),
    path('teachers/add/', exam_add, name='exam_add'),
    path('teachers/update/<int:pk>/', exam_update, name='exam_update'),
    path('teachers/<int:pk>/delete/', exam_delete, name='exam_delete'),
    path('teachers/<int:pk>/answers/', exam_answer_list, name='exam_answer_list'),
    path('teachers/<int:pk>/answers/check/', exam_answer_check, name='exam_answer_check'),

    path('students/', student_exam_home, name='exam_page_details_student'),
    path('students/submit/<int:pk>/', exam_submit, name='exam_submit')
]