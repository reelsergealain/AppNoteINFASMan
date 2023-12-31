from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse
from core.forms import SchoolYearForm, StudentForm

from core.models import SchoolYear, Student

def home(request):
    return render(request, 'core/home.html')


class StudentsListView(generic.ListView):
    model = Student
    template_name = 'core/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        return super().get_queryset()\
            .select_related('option', 'level')


class StudentCreateView(generic.CreateView):
    template_name = 'core/create_student.html'
    form_class = StudentForm

    def form_valid(self, form):
        form.save(True)
        return HttpResponseRedirect(reverse('core:student_list'))
    

class StudentUpdateView(generic.UpdateView):
    template_name = 'core/create_student.html'
    queryset = Student.objects.all()
    model = Student
    fields = [
            'student_id', 'first_name',
            'last_name', 'gender', 'birth_date',
            'email', 'phone', 'bourse', 'option', 'level',
        ]

    def form_valid(self, form):
        form.save(True)
        return HttpResponseRedirect(reverse('core:student_list'))


class SchoolYearListView(generic.ListView):
    model = SchoolYear
    template_name = "core/setting.html"
    context_object_name = 'school_year'


class SchoolYearCreateView(generic.CreateView):
    template_name = "core/create_school_year.html"
    form_class = SchoolYearForm

    def form_valid(self, form):
        form.save(True)
        return HttpResponseRedirect(reverse('core:student_list'))