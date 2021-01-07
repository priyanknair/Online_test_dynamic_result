from django.contrib import admin
from .models import Exam


class ExamAdmin(admin.ModelAdmin):
    list_display = ('Question', 'answer')


admin.site.register(Exam, ExamAdmin)

