from django.views.generic import TemplateView
from django.shortcuts import redirect
from planner.models import Student, Course, Planner



class IndexView(TemplateView):
    template_name = 'planner/index.html'


# Landing Page for Students after Login
class StudentLandingPageView(TemplateView):
    template_name = 'planner/landing_student.html'
    login_url = '/login/'
    redirect_field_name = 'next'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login/')
        elif not request.user.registered:
            return redirect('/login/')
        else:
            return super().dispatch(request, *args, **kwargs)
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = Student.objects.get(email=self.request.user.email)
        planners = student.planner_set.all()
        # planners = Planner.objects.filter(student=student)
        print(planners)
        sem_1 = planners[0].sem_one
        print(sem_1)
        enrolled_courses = [
            sem_1.class_one,
            sem_1.class_two,
            sem_1.class_three,
            sem_1.class_four,
            sem_1.class_five,
            sem_1.class_six
        ]
        context['enrolled_courses'] = enrolled_courses
        return context

# Course Plans View
class CoursePlansView(TemplateView) :
    template_name = 'planner/course_plans.html'

# Explore Major View
class ExploreMajorView( TemplateView):
    template_name = 'planner/explore_major.html'

