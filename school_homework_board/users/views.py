from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_homework')  # Замените 'home' на URL вашей домашней страницы
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})