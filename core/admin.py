from django.contrib import admin
from core.models import Student, SchoolYear, Level, Option

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(SchoolYear)
class SchoolYearAdmin(admin.ModelAdmin):
    pass


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    pass


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    pass
