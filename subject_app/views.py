from django.shortcuts import render
from .models import Subject
from .serializers import SubjectSerializer 
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

# def all_subjects(request):
#     subjects = SubjectSerializer(Subject.objects.all(), many=True) 
#     return JsonResponse({"subjects": subjects.data}) 

class All_subjects(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serialized_subjects = SubjectSerializer(subjects, many=True)
        return Response(serialized_subjects.data)
