from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(ModelViewSet):
# class StudentViewSet(ReadOnlyModelViewSet):
     queryset = Student.objects.all()
     serializer_class = StudentSerializer
