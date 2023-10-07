from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .decorators import staff_required
from .models import Homework, Answer
from django.contrib.auth.models import User
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
    students = User.objects.filter(is_staff=False)
    grades = {user: Answer.objects.filter(student=user).values_list('grade', flat=True) for user in students}
    return render(request, 'teacher_answers.html', {'students': students, 'grades': grades})