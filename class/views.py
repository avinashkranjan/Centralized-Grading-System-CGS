from django.shortcuts import render
import datetime
import calendar 

from .models import (
    Class, 
    Routine,
)

def class_view(request):
    day = datetime.datetime.today().isoweekday()
    
    if day < 7:
        day = day + 1
    else:
        day = day - 6

    routines = Routine.objects.filter(class_name__sem = request.user.student.sem)
    context = {
        'routines': routines,
        'todaysDay': day
    }

    return render(request, 'students/class_home.html', context)


# def  add_resources(request):
#     if request.user.is_authenticated:
#         if request.user.is_teacher:
#             if request.method == 'POST':
#                 form = classAddForm(request.POST, request.FILES)
#                 if form.is_valid():
#                     classes = form.save(commit=False)
#                     classes.teacher_name = request.user
#                     classes.save()
#                     return redirect('class_page')
#             else:
#                 form = ExamQuestionAddForm()
    
#             return render(request, 'teachers/class_add.html', {'form':form})
#         else:
#             return redirect('class_page')
#     return redirect('login')