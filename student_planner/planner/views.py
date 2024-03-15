from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

# Landing Page for Students after Login
class StudentLandingPageView(LoginRequiredMixin, TemplateView):
    template_name = 'landing_student.html'

# Course Plans View
class CoursePlansView(LoginRequiredMixin, TemplateView):
    template_name = 'course_plans.html'

# Explore Major View
class ExploreMajorView(LoginRequiredMixin, TemplateView):
    template_name = 'explore_major.html'