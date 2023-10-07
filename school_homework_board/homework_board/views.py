from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .decorators import staff_required
from .models import Homework, Answer
from .forms import AnswerForm

@login_required(login_url='users-login')
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

@staff_required(login_url='users-login')
def teacher_answers(request):
    answers = Answer.objects.all()
    return render(request, 'teacher_answers.html', {'answers': answers})