from rest_framework import serializers # import serializers from DRF
from .models import Student
from subject_app.serializers import SubjectSerializer

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student # specify what model this serializer is for
        fields = ['name', 'student_email', 'locker_number'] # specify the fields you would like this serializer to return. Alternatively if you would like to cover all fields at once you could use "__all__" within the fields list.

class StudentAllSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)
    class Meta:
        model = Student # specify what model this serializer is for
        # fields = '__all__'
        #exclude = ['id']
        fields = [
            "name",
            "student_email",
            "personal_email",
            "locker_number",
            "locker_combination",
            "good_student",
            "subjects",
        ]

    def get_subjects(self, obj):
        return SubjectSerializer(obj.students.all(), many=True).data