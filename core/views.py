from django.shortcuts import redirect, render
from django.urls import reverse
from core.forms import StudentForm

from core.models import Student

def home(request):
    return render(request, 'core/home.html')


def student_list(request):
    all_students = Student.objects.all()
    context = {
        'students': all_students
    }
    return render(request, 'core/student_list.html', context)


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('student_list'))  # Remplacez 'student_list' par l'URL de la liste des étudiants
    else:
        form = StudentForm()

    return render(request, 'core/create_student.html', {'form': form})