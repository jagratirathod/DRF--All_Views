from django.shortcuts import render
from.models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView  , CreateAPIView ,RetrieveAPIView ,UpdateAPIView , DestroyAPIView , ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCreate(CreateAPIView):
    queryset = Student
    serializer_class = StudentSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset = Student
    serializer_class = StudentSerializer

class StudentUpdate(UpdateAPIView):
    queryset = Student
    serializer_class = StudentSerializer

class StudentDestroy(DestroyAPIView):
    queryset = Student
    serializer_class = StudentSerializer

class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student
    serializer_class = StudentSerializer
