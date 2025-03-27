from rest_framework import serializers # import serializers from DRF
from .models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject # specify what model this serializer is for
        #fields = ['subject_name', 'professor', 'students', 'grade_average'] 
        fields = ['subject_name', 'professor']