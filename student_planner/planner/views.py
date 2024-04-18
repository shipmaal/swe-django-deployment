from typing import Any
from django.views.generic import TemplateView, FormView
from django.shortcuts import redirect
from planner.models import Student, Planner, Semester
from django.contrib import messages
from .api import PlanningCoursesAPI
from .forms import SemesterForm, PlannerForm



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
            # messages.error(request, 'You must be logged in to view this page.')
            return redirect('/login/')
        elif not request.user.registered:
            # messages.error(request, 'You must be registered to view this page.')
            return redirect('/register/')
        else:
            return super().dispatch(request, *args, **kwargs)
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = Student.objects.get(email=self.request.user.email)
        planners = Planner.objects.filter(student=student)
        if planners:
            sem_1 = planners[0].fall_one
            context['planners'] = planners
        
        return context

# Course Plans View
class CoursePlansView(TemplateView) :
    template_name = 'planner/course_plans.html'


# Course Plans View
class CreatePlanView(FormView) :
    form_class = PlannerForm
    template_name = 'planner/create_plan.html'
    success_url = '/create-plan/'

    def __init__(self, **kwargs):
        self.api = PlanningCoursesAPI('http://localhost:8080')
        super().__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = Student.objects.get(email=self.request.user.email)
        planners = Planner.objects.filter(student=student)

        if not planners:
            # Create empty semesters first
            semesters = [Semester.objects.create(credit_hours=0) for _ in range(8)]

            # Create the planner with the semesters
            planner = Planner.objects.create(
                student=student,
                fall_one=semesters[0],
                spring_one=semesters[1],
                fall_two=semesters[2],
                spring_two=semesters[3],
                fall_three=semesters[4],
                spring_three=semesters[5],
                fall_four=semesters[6],
                spring_four=semesters[7]
            )

            planners = Planner.objects.filter(student=student)
        
        for planner in planners:
            planner.semesters = [
                ('fall_one', planner.fall_one),
                ('spring_one', planner.spring_one),
                ('fall_two', planner.fall_two),
                ('spring_two', planner.spring_two),
                ('fall_three', planner.fall_three),
                ('spring_three', planner.spring_three),
                ('fall_four', planner.fall_four),
                ('spring_four', planner.spring_four),
            ]
        context['planners'] = planners

        return context
    
    def form_valid(self, form):
        student = Student.objects.get(email=self.request.user.email)
        semesters = [Semester.objects.create(credit_hours=0) for _ in range(8)]
        planner = Planner.objects.create(
            student=student,
            name=form.cleaned_data['name'],
            description=form.cleaned_data['description'],
            fall_one=semesters[0],
            spring_one=semesters[1],
            fall_two=semesters[2],
            spring_two=semesters[3],
            fall_three=semesters[4],
            spring_three=semesters[5],
            fall_four=semesters[6],
            spring_four=semesters[7]
        )

        return super().form_valid(form)

# Explore Major View
class ExploreMajorView(TemplateView):
    template_name = 'planner/explore_major.html'


class PlanSemester(FormView):
    form_class = SemesterForm
    template_name = 'planner/plan_semester.html'
    success_url = '../create-plan'
    def __init__(self, **kwargs: Any) -> None:
        self.api = PlanningCoursesAPI('https://localhost:8080')
        super().__init__(**kwargs)
    

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
        for course in selected_courses + optional_courses:
            if course:
                print(course.id)
                data = self.api.get_courses_by_code(course.id)
                credit_hours += data.course['creditOptionIds']
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

