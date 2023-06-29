from django.shortcuts import render
from.models import Student
from .serializer import StudentSerializer

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response


# Create your views here.


class StudentView(viewsets.ViewSet):

    def list(self,request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

    def create(self,request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'} , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        stu =  Student.objects.get(id=pk)
        serializer = StudentSerializer(stu , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data update'})
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

    
    def partial_update(self,request,pk):
        stu =  Student.objects.get(id=pk)
        serializer = StudentSerializer(stu , data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data update'})
        return Response(serializer.errors)

    def destroy(self,request,pk):
        stu =  Student.objects.get(id=pk)
        stu.delete()
        return Response({'msg' : 'Data Deleted'})






