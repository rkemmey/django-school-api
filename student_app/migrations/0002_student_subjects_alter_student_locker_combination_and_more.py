# Generated by Django 5.1.7 on 2025-03-26 18:00

import student_app.validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0001_initial'),
        ('subject_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(related_name='students', to='subject_app.subject'),
        ),
        migrations.AlterField(
            model_name='student',
            name='locker_combination',
            field=models.CharField(default='12-12-12', max_length=20, validators=[student_app.validator.validate_combination_format]),
        ),
        migrations.AlterField(
            model_name='student',
            name='locker_number',
            field=models.PositiveIntegerField(default=110, unique=True, validators=[student_app.validator.validate_locker_num]),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=255, validators=[student_app.validator.validate_name_format]),
        ),
        migrations.AlterField(
            model_name='student',
            name='personal_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_email',
            field=models.EmailField(max_length=254, unique=True, validators=[student_app.validator.validate_school_email]),
        ),
    ]
