from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('student-list', views.student_list, name='student_list'),
    path('create_student/', views.create_student, name='create_student')
]
