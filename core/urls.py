from django.urls import path, include
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('student-list', views.StudentsListView.as_view(), name='student_list'),
    path('eleves/ajouter/', views.StudentCreateView.as_view(), name='create_student'),
    path('eleves/<int:pk>/editer/', views.StudentUpdateView.as_view(), name='student_update'),
    path('create_schoolyear/', views.SchoolYearCreateView.as_view(), name='create_scholl_year'),
]
