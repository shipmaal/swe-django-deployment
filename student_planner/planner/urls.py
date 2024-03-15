from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('planner/', views.planner, name='planner'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('student-landing/', StudentLandingPageView.as_view(), name='landing_student'),
    path('course-plans/', CoursePlansView.as_view(), name='course_plans'),
    path('explore-major/', ExploreMajorView.as_view(), name='explore_major'),
]