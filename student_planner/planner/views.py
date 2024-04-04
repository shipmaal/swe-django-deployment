from typing import Any
from django.views.generic import TemplateView, FormView
from django.shortcuts import redirect
from planner.models import Student, Course, Planner, Subject, Semester
from .api import PlanningCoursesAPI
from .forms import SemesterForm
import dataclasses
import json
from django.shortcuts import render


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
            return redirect('/login/')
        elif not request.user.registered:
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
    def __init__(self, **kwargs):
        self.api = PlanningCoursesAPI('http://localhost:8080')
        super().__init__(**kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = Student.objects.get(email=self.request.user.email)
        object_list = Course.objects.filter(subject_area_id=student.major_one_id)
        print(object_list)
        context['object_list'] = object_list
        return context

# Explore Major View
class ExploreMajorView( TemplateView):
    template_name = 'planner/explore_major.html'


class PlanSemester(FormView):
    form_class = SemesterForm
    template_name = 'planner/plan_semester.html'
    success_url = '../create-plan'

    def form_valid(self, form):
        semester = Semester.objects.create()

        # Add the selected courses to the semester
        selected_courses = [
            form.cleaned_data['class_one'],
            form.cleaned_data['class_two'],
            form.cleaned_data['class_three'],
            form.cleaned_data['class_four']
        ]

        # Add optional courses if selected
        optional_courses = [
            form.cleaned_data['class_five'],
            form.cleaned_data['class_six']
        ]

        for course in selected_courses + optional_courses:
            if course:
                semester.courses.add(course)

        # Calculate and update credit hours
        '''
        credit_hours = 0
        for course in selected_courses:
        semester.credit_hours = credit_hours
        '''
        semester.save()
        return super().form_valid(form)
    '''
    def get_initial(self):
        if not self.request.user.is_authenticated:
            return {}
        
        initial = super().get_initial()
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        initial['email'] = self.request.user.email

        return initial
        '''

