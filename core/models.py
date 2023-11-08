from django.db import models

class Filiere(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)
    
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    bourse = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.last_name + ' ' + self.first_name


class Matter(models.Model):
    name = models.CharField(max_length=255)
    coefficient = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name) + ' ' + str(self.coefficient)


class SubMatter(models.Model):
    name = models.CharField(max_length=255)
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name) + ' - ' + str(self.matter)


class Assignment(models.Model):
    name = models.CharField(max_length=255)
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name) + ' - ' + str(self.matter)


class Exam(models.Model):
    name = models.CharField(max_length=255)
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name) + ' - ' + str(self.matter)


class Note(models.Model):
    SEMESTER_CHOICES = [
        ('1', '1er Sémestre'),
        ('2', '2eme Sémestre'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE)
    sub_matter = models.ForeignKey(SubMatter, on_delete=models.CASCADE, null=True, blank=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True, blank=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True, blank=True)
    note = models.DecimalField(max_digits=5, decimal_places=2)
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.matter} - {self.semester} - {self.note}"
