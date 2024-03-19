from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

class IndedxView(TemplateView):
    template_name = 'planner/index.html'

# Custom Login View
class CustomLoginView(TemplateView):
    template_name = 'planner/login.html'
    # redirect_authenticated_user = True

# Landing Page for Students after Login
class StudentLandingPageView( TemplateView):
    template_name = 'planner/landing_student.html'

# Course Plans View
class CoursePlansView(TemplateView) :
    template_name = 'planner/course_plans.html'

# Explore Major View
class ExploreMajorView( TemplateView):
    template_name = 'planner/explore_major.html'