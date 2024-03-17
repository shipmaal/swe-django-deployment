from django.contrib import admin
from .models import Student, Admin, Planner, Program, Course

# Register your models here.
admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Planner)
admin.site.register(Program)
admin.site.register(Course)
