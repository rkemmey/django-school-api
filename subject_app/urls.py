from django.urls import path
# Explicit imports
from .views import all_subjects
# all urls are prefaced by http://localhost:8000/api/v1/students/
urlpatterns = [
    # Currently only takes GET requests
    path('', all_subjects, name='all_subjects')
]