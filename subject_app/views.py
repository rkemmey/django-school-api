from django.shortcuts import render, get_object_or_404
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

class A_subject(APIView):
    # def get(self, request, name):
    #     subject = Subject.objects.get(name = name.title())
    #     return Response(SubjectSerializer(subject).data)
    def get(self, request, subject):
        subject = get_object_or_404(Subject, subject_name = subject.title())
        return Response(SubjectSerializer(subject).data)