from django.urls import path
# Explicit imports
from .views import All_students
# all urls are prefaced by http://localhost:8000/api/v1/students/
urlpatterns = [
    # Currently only takes GET requests
    #path('', all_students, name='all_students'),
    path("", All_students.as_view(), name='all_students'),
]