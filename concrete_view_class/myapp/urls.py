from django.urls import path
from . import views


urlpatterns = [
    # path('home/',views.home),
    path('list/',views.StudentList.as_view()),
    path('create/',views.StudentCreate.as_view()),
    path('retrieve/<int:pk>/',views.StudentRetrieve.as_view()),
    path('update/<int:pk>/',views.StudentUpdate.as_view()),
    path('destroy/<int:pk>/',views.StudentDestroy.as_view()),
    
    path('ListCreate/',views.StudentListCreate.as_view()),
    path('RetrieveUpdate/<int:pk>/',views.StudentRetrieveUpdateAPIView.as_view()),
    path('RetrieveUpdateDestroy/<int:pk>/',views.StudentRetrieveUpdateDestroy.as_view()),
]

