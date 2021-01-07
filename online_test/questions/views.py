from django.shortcuts import render
from questions.models import Exam




def examonline(request):
    results = Exam.objects.all()
    return render(request, 'index.html',{'Exam':results})