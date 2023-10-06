from django.shortcuts import render
from .models import Homework, Answer

def student_homework(request):
    homework = Homework.objects.all()
    return render(request, 'student_homework.html', {'homework': homework})

def teacher_answers(request):
    answers = Answer.objects.all()
    return render(request, 'teacher_answers.html', {'answers': answers})