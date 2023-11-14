from django.contrib import admin
from .models import (
    SchoolYear,
    Option,
    Level,
    Student,
    Subject,
    SubjectItem,
    OptionSubject,
    OptionSubjectItem,
    Grade,
    SemesterResult,
    AnnualResult,
)

# Enregistrement des modèles dans l'interface d'administration

@admin.register(SchoolYear)
class SchoolYearAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'student_id', 'option', 'level', 'school_year')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation')

@admin.register(SubjectItem)
class SubjectItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'code', 'subject')

@admin.register(OptionSubject)
class OptionSubjectAdmin(admin.ModelAdmin):
    list_display = ('subject', 'order')

@admin.register(OptionSubjectItem)
class OptionSubjectItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'option', 'subject', 'order', 'coefficient', 'max')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'grade_type', 'value', 'semester')

@admin.register(SemesterResult)
class SemesterResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'total_points', 'decimal_field', 'semester', 'rank')

@admin.register(AnnualResult)
class AnnualResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'total_points', 'average', 'rank')
