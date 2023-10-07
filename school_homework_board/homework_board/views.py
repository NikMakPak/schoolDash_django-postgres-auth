from django.shortcuts import render, redirect
from .models import Homework, Answer
from .forms import AnswerForm

def student_homework(request):
    homework = Homework.objects.all()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.student = request.user
            instance.save()
            return redirect('student_homework')
    else:
        form = AnswerForm()
    return render(request, 'student_homework.html', {'homework': homework, 'form': form})

def teacher_answers(request):
    answers = Answer.objects.all()
    return render(request, 'teacher_answers.html', {'answers': answers})