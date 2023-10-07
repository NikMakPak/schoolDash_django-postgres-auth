from django.db import models
from django.contrib.auth.models import User

class Homework(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    penalty_info = models.TextField()

    def __str__(self):
        return self.title

class Answer(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField(null=True)
    
    def __str__(self):
        return f'{self.homework} - {self.student.last_name} {self.student.first_name[0]}.'