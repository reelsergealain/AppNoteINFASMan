from django.db import models


class TimeStampedModel(models.Model):
    """ Cette classe est abstraite. Afin de réduire les repétitions
        des champs created_at et updated_at, toutes les tables qui
        ont ces champs doivent hériter de TimeStampedModel 
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SchoolYear(models.Model):
    name = models.CharField(max_length=9)

    class Meta:
        verbose_name = 'année scolaire'
    
    def __str__(self):
        return self.name
    

class Option(TimeStampedModel):
    name = models.CharField('nom', max_length=255)

    class Meta:
        verbose_name = 'filière'

    def __str__(self):
        return str(self.name)


class Level(models.Model):
    name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'niveau'

    def __str__(self):
        return self.abbreviation


class Student(TimeStampedModel):
    student_id = models.CharField('matricule', max_length=10)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    option = models.ForeignKey(Option, on_delete=models.PROTECT)
    bourse = models.BooleanField(default=False)
    level = models.ForeignKey(Level, on_delete=models.PROTECT)
    school_year = models.ForeignKey(SchoolYear, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'élève'

    def __str__(self):
        return self.last_name + ' ' + self.first_name


class Subject(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'matière'


class SubjectItem(TimeStampedModel):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=20)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'sous matière'

    def __str__(self):
        return str(self.name)


# Todo/A faire: Créer les tables relatives aux notes et établir les relations.  

# class Assignment(models.Model):
#     name = models.CharField(max_length=255)
#     matter = models.ForeignKey(Matter, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return str(self.name) + ' - ' + str(self.matter)


# class Exam(models.Model):
#     name = models.CharField(max_length=255)
#     matter = models.ForeignKey(Matter, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return str(self.name) + ' - ' + str(self.matter)


# class Note(models.Model):
#     SEMESTER_CHOICES = [
#         ('1', '1er Sémestre'),
#         ('2', '2eme Sémestre'),
#     ]
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     matter = models.ForeignKey(Matter, on_delete=models.CASCADE)
#     sub_matter = models.ForeignKey(SubMatter, on_delete=models.CASCADE, null=True, blank=True)
#     assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True, blank=True)
#     exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True, blank=True)
#     note = models.DecimalField(max_digits=5, decimal_places=2)
#     semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.student} - {self.matter} - {self.semester} - {self.note}"
