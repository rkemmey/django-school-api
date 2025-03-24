from django.db import models

# Create your models here.
# models.Model tell Django this is a Model that should be reflected on our database
class Student(models.Model):
    name = models.CharField(max_length=255, unique=False)
    student_email = models.EmailField(unique=True)
    personal_email = models.EmailField(unique=True)
    locker_number = models.PositiveIntegerField(unique=True, default=110)
    locker_combination = models.CharField(max_length=20, default="12-12-12")
    good_student = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_reassignment(self, new_locker_number):
        self.locker_number = new_locker_number
        self.save()

    def student_status(self, is_good):
        self.good_student = is_good
        self.save()