from rest_framework import serializers # import serializers from DRF
from .models import Subject
from django.db.models import Avg

class SubjectSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()
    grade_average = serializers.SerializerMethodField()
    class Meta:
        model = Subject # specify what model this serializer is for
        fields = ['subject_name', 'professor', 'students', 'grade_average'] 
        #fields = ['subject_name', 'professor']

    def get_students(self, instance):
        return instance.students.count()
    
    def get_grade_average(self, instance):
        average = instance.grades.aggregate(avg_grade=Avg('grade'))['avg_grade']
        return round(average, 2) if average is not None else None