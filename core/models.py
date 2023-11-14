from django.db import models

# Définition des choix pour les semestres
SEMESTER_1 = 1
SEMESTER_2 = 2
SEMESTER_CHOICES = [
    (SEMESTER_1, '1er Sémestre'),
    (SEMESTER_2, '2eme Sémestre'),
]

# Classe abstraite pour suivre les horodatages de création et de mise à jour
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # Date et heure de création automatique
    updated_at = models.DateTimeField(auto_now=True)      # Date et heure de mise à jour automatique

    class Meta:
        abstract = True  # Cette classe est abstraite

# Modèle pour représenter une année scolaire
class SchoolYear(models.Model):
    name = models.CharField(max_length=9)  # Nom de l'année scolaire, par exemple "2023-2024"

    class Meta:
        verbose_name = 'année scolaire'  # Nom convivial pour l'interface d'administration
    
    def __str__(self):
        return self.name

# Modèle pour représenter une filière
class Option(TimeStampedModel):
    name = models.CharField('nom', max_length=255)  # Nom de la filière, par exemple "Informatique"

    class Meta:
        verbose_name = 'filière'  # Nom convivial pour l'interface d'administration

    def __str__(self):
        return str(self.name)

# Modèle pour représenter un niveau académique
class Level(models.Model):
    name = models.CharField(max_length=20)          # Nom du niveau, par exemple "Licence"
    abbreviation = models.CharField(max_length=10)  # Abréviation du niveau, par exemple "L3"

    class Meta:
        verbose_name = 'niveau'  # Nom convivial pour l'interface d'administration

    def __str__(self):
        return self.abbreviation

# Modèle pour représenter un étudiant
class Student(TimeStampedModel):
    student_id = models.CharField('matricule', max_length=10)  # Matricule de l'étudiant
    first_name = models.CharField(max_length=255)             # Prénom de l'étudiant
    last_name = models.CharField(max_length=255)              # Nom de famille de l'étudiant
    birth_date = models.DateField()                            # Date de naissance de l'étudiant
    email = models.EmailField()                                # Adresse e-mail de l'étudiant
    phone = models.CharField(max_length=20)                   # Numéro de téléphone de l'étudiant
    option = models.ForeignKey(Option, on_delete=models.PROTECT)  # Filière de l'étudiant
    bourse = models.BooleanField(default=False)               # Indicateur de bourse
    level = models.ForeignKey(Level, on_delete=models.PROTECT)   # Niveau de l'étudiant
    school_year = models.ForeignKey(SchoolYear, on_delete=models.PROTECT)  # Année scolaire de l'étudiant

    class Meta:
        verbose_name = 'élève'  # Nom convivial pour l'interface d'administration

    def __str__(self):
        return self.last_name + ' ' + self.first_name

# Modèle pour représenter une matière
class Subject(models.Model):
    name = models.CharField(max_length=50)          # Nom de la matière
    abbreviation = models.CharField(max_length=50)  # Abréviation de la matière

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'matière'  # Nom convivial pour l'interface d'administration

# Modèle pour représenter une sous-matière
class SubjectItem(TimeStampedModel):
    name = models.CharField(max_length=255)       # Nom de la sous-matière
    abbreviation = models.CharField(max_length=20) # Abréviation de la sous-matière
    code = models.CharField(max_length=20, null=True)  # Code de la sous-matière (optionnel)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)  # Matière associée

    class Meta:
        verbose_name = 'sous matière'        # Nom convivial pour l'interface d'administration
        verbose_name_plural = 'sous matières'  # Nom convivial pour l'interface d'administration (au pluriel)

    def __str__(self):
        return str(self.name)

# Modèle pour associer une matière à une filière
class OptionSubject(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)  # Matière associée
    order = models.PositiveBigIntegerField(default=0)  # Ordre d'affichage

    class Meta:
        ordering = ['order']
        verbose_name = 'matière par filière'        # Nom convivial pour l'interface d'administration
        verbose_name_plural = 'matières par filière'  # Nom convivial pour l'interface d'administration (au pluriel)

# Modèle pour associer une sous-matière à une filière
class OptionSubjectItem(models.Model):
    name = models.CharField(max_length=50)            # Nom de la sous-matière
    option = models.ForeignKey(Option, on_delete=models.CASCADE)  # Filière associée
    subject = models.ForeignKey(OptionSubject, on_delete=models.CASCADE)  # Matière associée
    order = models.PositiveSmallIntegerField(default=1)  # Ordre d'affichage
    coefficient = models.PositiveSmallIntegerField(default=0)  # Coefficient de la sous-matière
    max = models.PositiveSmallIntegerField(default=20)  # Note maximale de la sous-matière

    class Meta:
        ordering = ['order']
        verbose_name = 'sous-matière par filière'        # Nom convivial pour l'interface d'administration
        verbose_name_plural = 'sous-matières par filière'  # Nom convivial pour l'interface d'administration (au pluriel)

# Modèle pour stocker les notes des étudiants
class Grade(TimeStampedModel):
    TYPE_EXAM = 'E'
    TYPE_TEST = 'D'
    TYPE_CHOICES = (
        (TYPE_EXAM, 'Examen'),
        (TYPE_TEST, 'Devoir'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Étudiant associé
    subject = models.ForeignKey(OptionSubjectItem, on_delete=models.CASCADE)  # Sous-matière associée
    grade_type = models.CharField(choices=TYPE_CHOICES, default=TYPE_EXAM,
                                  max_length=1)  # Type de note (Examen ou Devoir)
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Valeur de la note
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES)  # Semestre associé

    class Meta:
        verbose_name = 'note'  # Nom convivial pour l'interface d'administration

    def __str__(self):
        return f"{self.student} - {self.semester} - {self.value}"

# Modèle pour stocker les résultats par semestre
class SemesterResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Étudiant associé
    total_points = models.DecimalField(max_digits=4, decimal_places=2)  # Total des points
    decimal_field = models.DecimalField(max_digits=4, decimal_places=2)  # Champ décimal (non spécifié dans le commentaire)
    semester = models.PositiveSmallIntegerField(choices=SEMESTER_CHOICES)  # Semestre associé
    rank = models.PositiveSmallIntegerField()  # Classement de l'étudiant dans le semestre

    class Meta:
        verbose_name = 'résultat par semestre'  # Nom convivial pour l'interface d'administration

    def __str__(self):
        return f'{self.student} -> {self.average}'  # Affichage du résultat

# Modèle pour stocker les résultats généraux annuels
class AnnualResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Étudiant associé
    total_points = models.DecimalField(max_digits=4, decimal_places=2)  # Total des points
    average = models.DecimalField(max_digits=4, decimal_places=2)  # Moyenne générale
    rank = models.PositiveSmallIntegerField()  # Classement de l'étudiant

    class Meta:
        verbose_name = 'résultat général annuel'  # Nom convivial pour l'interface d'administration

    def __str__(self):
        return f'{self.student} -> {self.average} (MGA)'  # Affichage du résultat
