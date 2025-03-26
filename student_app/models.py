from django.db import models
from .validator import validate_name_format, validate_school_email, validate_combination_format, validate_locker_num
from subject_app.models import Subject

# Create your models here.
# models.Model tell Django this is a Model that should be reflected on our database
class Student(models.Model):
    name = models.CharField(max_length=255, unique=False, validators=[validate_name_format])
    student_email = models.EmailField(unique=True, validators=[validate_school_email])
    personal_email = models.EmailField(unique=True)
    locker_number = models.PositiveIntegerField(unique=True, default=110, validators=[validate_locker_num])
    locker_combination = models.CharField(max_length=20, default="12-12-12", validators=[validate_combination_format])
    good_student = models.BooleanField(default=True)
    subjects = models.ManyToManyField(Subject, related_name='students')

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_reassignment(self, new_locker_number):
        self.locker_number = new_locker_number
        self.save()

    def student_status(self, is_good):
        self.good_student = is_good
        self.save()

    def add_subject(self, subject_id):
        msg_error = "This students class schedule is full!"
        sub_length = self.subjects.count()
        if sub_length < 8:
            self.subjects.add(subject_id)
        else:
            raise Exception(msg_error)

    def remove_subject(self, subject_id):
        msg_error = "This students class schedule is empty!"
        sub_length = self.subjects.count()
        if sub_length > 0:
            self.subjects.remove(subject_id)
        else:
            raise Exception(msg_error)