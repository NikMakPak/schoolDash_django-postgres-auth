from django.contrib import admin
from .models import Homework, Answer

class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'teacher', 'due_date')
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date_created')

admin.site.register(Homework, HomeworkAdmin)
admin.site.register(Answer, AnswerAdmin)