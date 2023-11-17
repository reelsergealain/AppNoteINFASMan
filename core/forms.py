from django import forms
from .models import SchoolYear, Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_id',
            'first_name',
            'last_name',
            'gender',
            'birth_date',
            'email',
            'phone',
            'option',
            'bourse',
            'level',
        ]

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')

        if not phone.isdigit() or len(phone) != 10:
            raise forms.ValidationError("Le numéro de téléphone doit avoir exactement 10 chiffres.")

        valid_prefixes = ['01', '07', '05']
        if not any(phone.startswith(prefix) for prefix in valid_prefixes):
            raise forms.ValidationError("Le numéro de téléphone doit commencer par 01, 07, ou 05.")

        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email', '')

        if not email.endswith('infas.edu.ci'):
            raise forms.ValidationError("L'adresse e-mail doit se terminer par 'infas.edu.ci'.")

        return email

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['option'].initial = self.fields['option'].queryset.first()
        self.fields['level'].initial = self.fields['level'].queryset.first()
        self.add_bootstrap_styles()

    def add_bootstrap_styles(self):
        field_classes = 'form-control'
        checkbox_class = 'form-check-input'
        datepicker_class = 'datepicker'

        placeholders = {
            'student_id': 'Matricule',
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'email': 'Adresse e-mail',
            'phone': 'Numéro de téléphone',
        }

        for field_name, field in self.fields.items():
            widget_class = field.widget.attrs.get('class', '')
            widget_class += f' {field_classes}' if field_name != 'bourse' else f' {checkbox_class}'
            widget_class += f' {datepicker_class}' if field_name == 'birth_date' else ''
            field.widget.attrs['class'] = widget_class.strip()

            placeholder = placeholders.get(field_name)
            if placeholder:
                field.widget.attrs['placeholder'] = placeholder

class SchoolYearForm(forms.ModelForm):
    class Meta:
        model = SchoolYear
        fields = [
            'name',
        ]
    def __init__(self, *args, **kwargs):
        super(SchoolYearForm, self).__init__(*args, **kwargs)
        self.add_bootstrap_styles()

    def add_bootstrap_styles(self):
        field_classes = 'form-control'

        placeholders = {
            'name': '2022-2023',
        }

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = field_classes

            placeholder = placeholders.get(field_name)
            if placeholder:
                field.widget.attrs['placeholder'] = placeholder