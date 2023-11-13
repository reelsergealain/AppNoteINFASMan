from django.shortcuts import render

from core.models import Student

def home(request):
    return render(request, 'core/home.html')


def student_list(request):
    all_students = Student.objects.all()
    context = {
        'students': all_students
    }
    return render(request, 'core/student_list.html', context)