from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentLandingPageView.as_view(), name='landing_student'),
    path('landing-student', views.StudentLandingPageView.as_view(), name='landing_student'),
    path('course-plans/', views.CoursePlansView.as_view(), name='course_plans'),
    path('explore-major/', views.ExploreMajorView.as_view(), name='explore_major'),
]