from django.db import models

class Role(models.Model):
    name = models.TextField()

class User(models.Model):
    name = models.TextField()
    email = models.TextField()
    password_hash = models.TextField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

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