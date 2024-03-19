from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndedxView.as_view(), name='index'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('student-landing/', views.StudentLandingPageView.as_view(), name='landing_student'),
    path('course-plans/', views.CoursePlansView.as_view(), name='course_plans'),
    path('explore-major/', views.ExploreMajorView.as_view(), name='explore_major'),
]