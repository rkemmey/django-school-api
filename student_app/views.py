from django.shortcuts import render, get_object_or_404
from .models import Student
from .serializers import StudentAllSerializer 
#from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

# def all_students(request):
#     students = StudentAllSerializer(Student.objects.all(), many=True) 
#     return JsonResponse({"students": students.data}) 

class All_students(APIView):
    def get(self, request):
        students = Student.objects.all()
        serialized_students = StudentAllSerializer(students, many=True)
        return Response(serialized_students.data)
    
class A_student(APIView):
    def get(self, request, id):
        student = get_object_or_404(Student, id = id)
        return Response(StudentAllSerializer(student).data)