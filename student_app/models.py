from django.db import models

# Create your models here.
# models.Model tell Django this is a Model that should be reflected on our database
class Student(models.Model):
    name = models.CharField(max_length=255)
    student_email = models.EmailField(unique=True)
    personal_email = models.EmailField(blank=True, null=True)
    locker_number = models.PositiveIntegerField(unique=True)
    locker_combination = models.CharField(max_length=10)
    good_student = models.BooleanField(default=True)

    def __str__(self):
        return self.name