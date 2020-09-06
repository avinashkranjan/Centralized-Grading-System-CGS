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

    routines = Routine.objects.filter(class_name__sem=request.user.student.sem)
    context = {
        'routines': routines,
        'todaysDay': day
    }

    return render(request, 'students/class_home.html', context)
