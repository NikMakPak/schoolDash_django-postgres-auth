from django.contrib import admin
from django.urls import path,include 
from homework_board.views import student_homework, teacher_answers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_homework/', student_homework, name='student_homework'),
    path('teacher_answers/', teacher_answers, name='teacher_answers'),
    path('', include('users.urls'))
]