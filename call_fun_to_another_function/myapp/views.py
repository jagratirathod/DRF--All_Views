from django.shortcuts import render
from django.http import HttpResponse
from . models import Student

# Create your views here.


def function1(*request):
    save = function2(request)
    print(save)
    return HttpResponse(save)
    
def function2(request):
    queryset = Student.objects.get(id=1)
    city = queryset.city
    return HttpResponse(queryset,city)


def wage(w_hours):
    return w_hours*25

def with_bonus(hours):
    return wage(hours) + 50

wage(8) , with_bonus(8)


