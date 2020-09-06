from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator

from .forms import *
from .decorators import *
from .models import *


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers:assignment_page')
        else:
            return redirect('students:assignment_page')
    return redirect('login')


#<------teachers-view---------->

@login_required
@teacher_required
def assignment_home(request):
    assignments = Assignment.objects.filter(owner_id = request.user.id)
    num = int(0)
    context = {
        'assignments' : assignments,
        'num' : num
    }

    return render(request, 'teachers/assignment_home.html', context)


@login_required
@teacher_required
def assignment_add(request):
    if request.method == 'POST':
        form = AssignmentAddForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.owner = request.user
            assignment.save()
            return redirect('teachers:assignment_page')
    else:
        form = AssignmentAddForm()
    
    return render(request, 'teachers/assignment_add.html', {'form':form})


@login_required
@teacher_required
def assignment_update(request, pk):
    assignment = Assignment.objects.get(pk=pk)
    if request.method == 'POST':
        form = AssignmentAddForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.owner = request.user
            assignment.save()
            return redirect('assignment_page')
    else:
        form = AssignmentAddForm(instance=assignment)
    
    return render(request, 'teachers/assignment_update.html', {'form':form, 'assignment':assignment})


@login_required
@teacher_required
def assignment_delete(request,pk):
    assignment = Assignment.objects.get(pk=pk)
    assignment.delete()

    return redirect('teachers:assignment_page')


@login_required
@teacher_required
def submitted_assignment(request,pk):
    answers = StudentAnswer.objects.filter(assignment__id = pk)
    context ={
        'answers': answers,
    }
    
    return render(request, 'teachers/submitted_assignment.html', context)


#<-----------Students-view----------->

@login_required
@student_required
def student_assignment_home(request):
    sem = request.user.student.sem

    assignments = Assignment.objects.filter(subject__sem = sem)
    num = int(0)
    context = {
        'assignments' : assignments,
        'num' : num
    }

    return render(request, 'students/assignment_home.html', context)


@login_required
@student_required
def student_assignment_upload(request, pk):
    assignment = Assignment.objects.get(pk = pk)
    if request.method == 'POST':
        form = AssignmentSubmitForm(request.POST, request.FILES)
        if form.is_valid():
            studentanswer = form.save(commit=False)
            studentanswer.student = request.user.student
            studentanswer.assignment = assignment
            studentanswer.save()
            return redirect('students:assignment_page')
    else:
        form = AssignmentSubmitForm()
    
    return render(request, 'students/assignment_upload.html', {'form':form})
        



