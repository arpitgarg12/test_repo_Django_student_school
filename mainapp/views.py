from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse

# Mainapp Imports
from . models import School, Student
from .forms import SchoolForm, StudentForm

# Create your views here.

class BaseView(View):
    def get(self, request):
        return render(request, 'base.html')


class SchoolCreateView(View):
    def get(self, request):
        form = SchoolForm()
        return render(request, 'school_create.html', {'form': form})

    def post(self, request):
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('school_list')
        return render(request, 'school_create.html', {'form': form})


class SchoolUpdateView(View):
    def get(self, request, pk):
        school = School.objects.get(pk=pk)
        form = SchoolForm(instance=school)
        return render(request, 'school_update.html', {'form': form, 'school': school})

    def post(self, request, pk):
        school = School.objects.get(pk=pk)
        form = SchoolForm(request.POST, instance=school)
        if form.is_valid():
            form.save()
            return redirect('school_list')
        return render(request, 'school_update.html', {'form': form, 'school': school})


class SchoolDeleteView(View):
    def post(self, request, pk):
        school = School.objects.get(pk=pk)
        school.delete()
        return JsonResponse({'status': True, 'message': 'School deleted successfully'})


class SchoolListView(View):
    def get(self, request):
        schools = School.objects.all()
        return render(request, 'school_list.html', {'school': schools})


class StudentCreateView(View):
    def get(self, request):
        form = StudentForm()
        return render(request, 'student_create.html', {'form': form})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        return render(request, 'student_create.html', {'form': form})


class StudentUpdateView(View):
    def get(self, request, pk):
        student = Student.objects.get(pk=pk)
        form = StudentForm(instance=student)
        return render(request, 'student_update.html', {'form': form, 'student': student})

    def post(self, request, pk):
        student = Student.objects.get(pk=pk)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        return render(request, 'student_update.html', {'form': form, 'student': student})


class StudentDeleteView(View):
    def post(self, request, pk):
        student = Student.objects.get(pk=pk)
        student.delete()
        return JsonResponse({'status': True, 'message': 'Student deleted successfully'})


class StudentListView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, 'student_list.html', {'student': students})
