from django.urls import path
# Explicit imports
#from .views import all_subjects
from .views import All_subjects, A_subject
# all urls are prefaced by http://localhost:8000/api/v1/students/
urlpatterns = [
    # Currently only takes GET requests
    #path('', all_subjects, name='all_subjects')
    path('', All_subjects.as_view(), name='all_subjects'),
    path('<str:subject>/', A_subject.as_view(), name="a_subject"),
]