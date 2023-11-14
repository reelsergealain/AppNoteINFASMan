from django.db import models

SEMESTER_1 = 1
SEMESTER_2 = 2
SEMESTER_CHOICES = [
    (SEMESTER_1, '1er Sémestre'),
    (SEMESTER_2, '2eme Sémestre'),
]


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
    code = models.CharField(max_length=20, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'sous matière'
        verbose_name_plural = 'sous matières'

    def __str__(self):
        return str(self.name)


class OptionSubject(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    order = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'matière par filière'
        verbose_name_plural = 'matières par filière'


class OptionSubjectItem(models.Model):
    name = models.CharField(max_length=50)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    subject = models.ForeignKey(OptionSubject, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(default=1)
    coefficient = models.PositiveSmallIntegerField(default=0)
    max = models.PositiveSmallIntegerField(default=20)

    class Meta:
        ordering = ['order']
        verbose_name = 'sous-matière par filière'
        verbose_name_plural = 'sous-matières par filière'


class Grade(TimeStampedModel):
    TYPE_EXAM = 'E'
    TYPE_TEST = 'D'
    TYPE_CHOICES = (
        (TYPE_EXAM, 'Examen'),
        (TYPE_TEST, 'Devoir'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(OptionSubjectItem, on_delete=models.CASCADE)
    grade_type = models.CharField(choices=TYPE_CHOICES, default=TYPE_EXAM, 
                                  max_length=1)
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES)

    class Meta:
        verbose_name = 'note'

    def __str__(self):
        return f"{self.student} - {self.semester} - {self.value}"


class SemesterResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_points = models.DecimalField(max_digits=4, decimal_places=2)
    decimal_field = models.DecimalField(max_digits=4, decimal_places=2)
    semester = models.PositiveSmallIntegerField(choices=SEMESTER_CHOICES)
    rank = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'résultat par semestre'

    def __str__(self):
        return f'{self.student} -> {self.average}'


class AnnualResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_points = models.DecimalField(max_digits=4, decimal_places=2)
    average = models.DecimalField(max_digits=4, decimal_places=2)
    rank = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'résultat général annuel'

    def __str__(self):
        return f'{self.student} -> {self.average} (MGA)'
    