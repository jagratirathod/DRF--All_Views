from django.contrib import admin
from django.urls import path,include
from myapp import views

from rest_framework.routers import DefaultRouter
from rest_framework import routers


router = DefaultRouter()
router.register('student', views.StudentView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
