from django.urls import path, include
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('student-list', views.StudentsListView.as_view(), name='student_list'),
    path('create_student/', views.StudentCreateView.as_view(), name='create_student')
]
