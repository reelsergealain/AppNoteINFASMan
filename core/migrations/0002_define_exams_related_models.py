# Generated by Django 4.2.7 on 2023-11-14 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveBigIntegerField(default=0)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subject')),
            ],
            options={
                'verbose_name': 'matière par filière',
                'verbose_name_plural': 'matières par filière',
                'ordering': ['order'],
            },
        ),
        migrations.AlterModelOptions(
            name='subjectitem',
            options={'verbose_name': 'sous matière', 'verbose_name_plural': 'sous matières'},
        ),
        migrations.AddField(
            model_name='subjectitem',
            name='code',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='SemesterResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_points', models.DecimalField(decimal_places=2, max_digits=4)),
                ('decimal_field', models.DecimalField(decimal_places=2, max_digits=4)),
                ('semester', models.PositiveSmallIntegerField(choices=[(1, '1er Sémestre'), (2, '2eme Sémestre')])),
                ('rank', models.PositiveSmallIntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
            ],
            options={
                'verbose_name': 'résultat par semestre',
            },
        ),
        migrations.CreateModel(
            name='OptionSubjectItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('order', models.PositiveSmallIntegerField(default=1)),
                ('coefficient', models.PositiveSmallIntegerField(default=0)),
                ('max', models.PositiveSmallIntegerField(default=20)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.option')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.optionsubject')),
            ],
            options={
                'verbose_name': 'sous-matière par filière',
                'verbose_name_plural': 'sous-matières par filière',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('grade_type', models.CharField(choices=[('E', 'Examen'), ('D', 'Devoir')], default='E', max_length=1)),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('semester', models.CharField(choices=[(1, '1er Sémestre'), (2, '2eme Sémestre')], max_length=1)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.optionsubjectitem')),
            ],
            options={
                'verbose_name': 'note',
            },
        ),
        migrations.CreateModel(
            name='AnnualResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_points', models.DecimalField(decimal_places=2, max_digits=4)),
                ('average', models.DecimalField(decimal_places=2, max_digits=4)),
                ('rank', models.PositiveSmallIntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
            ],
            options={
                'verbose_name': 'résultat général annuel',
            },
        ),
    ]
