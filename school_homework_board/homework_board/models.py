from django.db import models
from django.contrib.auth.models import User

class Homework(models.Model):
    title = models.TextField()
    subject = models.TextField()
    teacher = models.TextField()
    description = models.TextField()
    due_date = models.DateField()
    penalty_info = models.TextField()

class Answer(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_text = models.TextField()
    submitted_at = models.DateTimeField()
    grade = models.IntegerField()