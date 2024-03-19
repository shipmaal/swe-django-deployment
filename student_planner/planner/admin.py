from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student, User, Advisor, Planner, Course, Major, Minor

# Register your models here.
admin.site.register(Student)
admin.site.register(User, UserAdmin)
admin.site.register(Advisor)
admin.site.register(Planner)
admin.site.register(Course)
admin.site.register(Major)
admin.site.register(Minor)

