from django.shortcuts import render
from books.models import Subject


def subject(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'main/navbar.html', context)
