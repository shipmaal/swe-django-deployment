from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



class IndedxView(TemplateView):
    template_name = 'planner/index.html'


# Landing Page for Students after Login
@method_decorator(login_required, name='dispatch')
class StudentLandingPageView(LoginRequiredMixin, TemplateView):
    template_name = 'planner/landing_student.html'
    login_url = '/login/'
    redirect_field_name = 'next'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.registered:
                return redirect('login')  # Modify this line
        else:
            return super().dispatch(request, *args, **kwargs)
        

# Course Plans View
class CoursePlansView(TemplateView) :
    template_name = 'planner/course_plans.html'

# Explore Major View
class ExploreMajorView( TemplateView):
    template_name = 'planner/explore_major.html'

