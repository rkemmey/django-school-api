from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer 
from django.http import JsonResponse
# Create your views here.

def all_students(request):
    students = StudentSerializer(Student.objects.all(), many=True) 
    return JsonResponse({"students": students.data}) 

def all_subjects(request):
    subjects = StudentSerializer(Student.objects.all(), many=True) 
    return JsonResponse({"subjects": subjects.data}) 