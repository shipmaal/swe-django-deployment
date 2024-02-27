from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'planner/login.html')

def planner(request):
    return render(request, 'planner/landing_student.html')