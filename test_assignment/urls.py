"""
URL configuration for test_assignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Importing Views for routing
from mainapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseView.as_view(), name='base'),
    # School urls
    path('school/create/', SchoolCreateView.as_view(), name='school_create'),
    path('school/update/<int:pk>/',
         SchoolUpdateView.as_view(), name='school_update'),
    path('school/delete/<int:pk>/',
         SchoolDeleteView.as_view(), name='school_delete'),
    path('school/list/', SchoolListView.as_view(), name='school_list'),
    # Student urls
    path('student/create/', StudentCreateView.as_view(), name='student_create'),
    path('student/update/<int:pk>/',
         StudentUpdateView.as_view(), name='student_update'),
    path('student/delete/<int:pk>/',
         StudentDeleteView.as_view(), name='student_delete'),
    path('student/list/', StudentListView.as_view(), name='student_list'),

]
