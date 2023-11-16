from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse
from core.forms import StudentForm

from core.models import Student

def home(request):
    return render(request, 'core/home.html')


class StudentsListView(generic.ListView):
    model = Student
    template_name = 'core/student_list.html'
    context_object_name = 'students'


class StudentCreateView(generic.CreateView):
    template_name = 'core/create_student.html'
    form_class = StudentForm

    def form_valid(self, form):
        form.save(True)
        return HttpResponseRedirect(reverse('core:student_list'))