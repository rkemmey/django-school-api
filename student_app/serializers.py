from rest_framework import serializers # import serializers from DRF
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student # specify what model this serializer is for
        fields = ['name', 'student_email', 'locker_number'] # specify the fields you would like this serializer to return. Alternatively if you would like to cover all fields at once you could use "__all__" within the fields list.

class StudentAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student # specify what model this serializer is for
        # fields = '__all__'
        exclude = ['id']