from django.db import models
from .validators import validate_professor_name, validate_subject_format

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(blank=False, null=False, unique=True, validators=[validate_subject_format])
    professor = models.CharField(blank=False, null=False, validators=[validate_professor_name])
    #students MtM exists in student_app.models.py

    def __str__(self):
        return f"{self.subject_name} - {self.professor} - {self.students.count()}"
    
    def add_a_student(self, student_id):
        stud_length = self.students.count()
        if stud_length < 31:
            self.students.add(student_id)
        else:
            raise Exception("This subject is full!")
    
    def drop_a_student(self, student_id):
        stud_length = self.students.count()
        if stud_length > 0:
            self.students.remove(student_id)
        else:
            raise Exception("This subject is empty!")