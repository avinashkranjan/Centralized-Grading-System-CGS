from django.db import models

from assignment.models import (
    User,
)


class Teacher(models.Model):
    teacher = models.OneToOneField(User, verbose_name= "Name of Teacher", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.teacher.username
    

class Class(models.Model):
    class_name = models.CharField(verbose_name="Name of Subject", max_length = 100)
    teacher_name = models.ForeignKey(Teacher, verbose_name= "Name of Teacher", on_delete=models.CASCADE)
    sem = models.PositiveIntegerField(verbose_name="Semister")
    course_time = models.PositiveIntegerField(verbose_name="Total study Hour")

    def __str__(self):
        return str(self.class_name)
    
    

class Routine(models.Model):
    day = models.PositiveIntegerField(verbose_name="Day of week in integer")
    class_name = models.ForeignKey("class.Class", on_delete=models.CASCADE, verbose_name="Subject Name")
    start_time = models.TimeField(verbose_name="Class start time")
    end_time = models.TimeField(verbose_name="Class end time")
    class_link = models.CharField(verbose_name="Link for online class", max_length = 100)

    def __str__(self):

        day_name = ""
        if self.day == 1:
            day_name = "Sunday"
        elif self.day == 2:
            day_name = "Monday"
        elif self.day == 3:
            day_name = "Tuesday"
        elif self.day == 4:
            day_name = "Wednesday"
        elif self.day == 5:
            day_name = "Thursday"
        elif self.day == 6:
            day_name = "Friday"
        else:
            day_name == "Saturday"

        return day_name + " - " + str(self.class_name) 
    

# class Resources(models.Model):
#     def user_directory_path(instance, filename):
#         return 'class/{0}/{1}'.format(routine.day, routine.class_name)
#     routine = models.ForeignKey(Routine, on_delete=models.CASCADE, verbose_name="Routine - Subject")
#     file1 = models.FileField(upload_to=user_directory_path)
#     file2 = models.FileField(upload_to=user_directory_path)
#     file3 = models.FileField(upload_to=user_directory_path)
