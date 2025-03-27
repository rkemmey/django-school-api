from django.shortcuts import render
from .models import Subject
from .serializers import SubjectSerializer 
from django.http import JsonResponse
# Create your views here.

def all_subjects(request):
    subjects = SubjectSerializer(Subject.objects.all(), many=True) 
    return JsonResponse({"subjects": subjects.data}) 
