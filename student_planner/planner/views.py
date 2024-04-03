from typing import Any
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import messages
from planner.models import Student, Planner
from .api import PlanningCoursesAPI
import dataclasses
import json


class IndexView(TemplateView):
    template_name = 'planner/index.html'


# Landing Page for Students after Login
class StudentLandingPageView(TemplateView):
    template_name = 'planner/landing_student.html'
    redirect_field_name = 'next'

    def __init__(self, **kwargs: Any) -> None:
        self.api = PlanningCoursesAPI('http://localhost:8080')
        super().__init__(**kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to view this page.')
            return redirect('/login/')
        elif not request.user.registered:
            messages.error(request, 'You must be registered to view this page.')
            return redirect('/register/')
        else:
            return super().dispatch(request, *args, **kwargs)
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = Student.objects.get(email=self.request.user.email)
        planners = Planner.objects.filter(student=student)
        if planners:
            sem_1 = planners[0].sem_one
            enrolled_courses = [
                sem_1.class_one,
                sem_1.class_two,
                sem_1.class_three,
                sem_1.class_four,
                sem_1.class_five,
                sem_1.class_six
            ]
           
            data = self.api.get_courses_by_code('CSCI1074')
            context['data'] = data
            data_dict = dataclasses.asdict(data[0])
            data = self.api.get_all_courses()
            subject = data[0].subjectArea
            course = data[0].course
           
            context['data_dict'] = json.dumps(data_dict)
            context['enrolled_courses'] = enrolled_courses
            context['planners'] = planners
        
        return context

# Course Plans View
class CoursePlansView(TemplateView) :
    template_name = 'planner/course_plans.html'

# Course Plans View
class CreatePlanView(TemplateView) :
    template_name = 'planner/create_plan.html'

# Explore Major View
class ExploreMajorView( TemplateView):
    template_name = 'planner/explore_major.html'

