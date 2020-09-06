from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from .models import *

from assignment.models import (
    User,
    Student,
)


def exam_view(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('exam_page_details_teacher')
        else:
            return redirect('exam_page_details_student')
    return redirect('login')


'''

Teachers Views

'''


def exam_home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            exams = ExamQuestions.objects.filter(owner_id=request.user.id)
            context = {
                'exams': exams,
            }

            return render(request, 'teachers/exam_home.html', context)
        else:
            return redirect('exam_page_details_student')
    return redirect('login')


def exam_add(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            if request.method == 'POST':
                form = ExamQuestionAddForm(request.POST, request.FILES)
                if form.is_valid():
                    exam = form.save(commit=False)
                    exam.owner = request.user
                    exam.save()
                    return redirect('exam_page_details_teacher')
            else:
                form = ExamQuestionAddForm()

            return render(request, 'teachers/exam_add.html', {'form': form})
        else:
            return redirect('exam_page_details_student')
    return redirect('login')


def exam_update(request, pk):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            exam = ExamQuestions.objects.get(pk=pk)
            if request.method == 'POST':
                form = ExamQuestionAddForm(request.POST, request.FILES)
                if form.is_valid():
                    exam = form.save(commit=False)
                    exam.owner = request.user
                    exam.save()
                    return redirect('exam_page_details_teacher')
            else:
                form = ExamQuestionAddForm(instance=exam)

            return render(request, 'teachers/exam_update.html', {'form': form, 'exam': exam})
        else:
            return redirect('exam_page_details_student')
    return redirect('login')


def exam_delete(request, pk):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            exam = ExamQuestions.objects.get(pk=pk)
            exam.delete()

            return redirect('exam_page_details_teacher')
        else:
            return redirect('exam_page_details_student')
    return redirect('login')


def exam_answer_list(request, pk):
    answers = ExamAnswers.objects.filter(examQuestions_id=pk)
    for answer in answers:
        print(answer.student.user.username)
    context = {
        'answers': answers,
    }

    return render(request, 'teachers/answer_list.html', context)


def exam_answer_check(request, pk):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            answer = ExamAnswers.objects.get(pk=pk)
            if request.method == 'POST':
                form = ExamAnswerCheckForm(request.POST)
                if form.is_valid():
                    exam = form.save(commit=False)
                    exam.student = Student.objects.get(pk=answer.student.id)
                    exam.examQuestions = ExamQuestions(
                        pk=answer.examQuestions.id)
                    exam.total_marks_obtained = form.cleaned_data.get(
                        'question1_marks') + form.cleaned_data.get('question2_marks') + form.cleaned_data.get('question3_marks')
                    exam.save()
                    return redirect('exam_page_details_teacher')
                else:
                    return HttpResponse("error")
            else:
                answer = ExamAnswers.objects.get(pk=pk)
                print(answer)
                form = ExamAnswerCheckForm(instance=answer)
                exam = ExamQuestions(pk=answer.examQuestions.id)
                print(exam.question1)

                return render(request, 'teachers/exam_answer_check.html', {
                    'form': form,
                    'exam': exam,
                    'answer': answer,
                })
        else:
            return redirect('exam_page_details_student')
    return redirect('login')


'''

Student Views

'''


def student_exam_home(request):
    if request.user.is_authenticated:
        if request.user.is_student:
            exams = ExamQuestions.objects.filter(
                subject__sem=request.user.student.sem)
            context = {
                'exams': exams,
            }
            return render(request, 'students/exam.html', context)
        else:
            return redirect('exam_page_details_student')
    return redirect('login')


def exam_submit(request, pk):
    if request.user.is_authenticated:
        if request.user.is_student:
            if request.method == 'POST':
                form = ExamAnswerAddForm(request.POST, request.FILES)
                if form.is_valid():
                    exam = form.save(commit=False)
                    exam.student = request.user.student
                    exam.examQuestions = ExamQuestions.objects.get(pk=pk)
                    exam.save()
                    return redirect('exam_page_details_student')
            else:

                if not check_attendence:
                    form = ExamAnswerAddForm()
                    exam = ExamQuestions.objects.get(pk=pk)
                    context = {
                        'exam': exam,
                        'form': form,
                    }
                else:
                    return redirect('exam_page_details_student')

            return render(request, 'students/exam_submit.html', context)
        else:
            return redirect('exam_page_details_student')
    return redirect('login')
