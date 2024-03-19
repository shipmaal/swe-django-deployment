import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Student(models.Model):
    def __str__(self):
        return self.eagle_id
    eagle_id = models.CharField(max_length=8)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length = 254)
    class_year = models.CharField(max_length=4)
    end_semester = models.CharField(max_length=6, default="Spring")
    major_one = models.ForeignKey(Major, default=None)
    major_two = models.ForeignKey(Major, default=None)
    minor_one = models.ForeignKey(Major, default=None)
    minor_two = models.ForeignKey(Major, default=None)

    class College(models.TextChoices):
        MCAS = "MCAS", _("Morrissey College of Arts and Sciences")
        CSOM = "CSOM", _("Carroll School of Management")
        CSON = "CSON", _("William F. Connell School of Nursing")
        LYNCH = "LYNCH", ("Carolyn A. and Peter S. Lynch School of Education and Human Development")
    
    college = models.CharField(
        max_length=5,
        choices=College,
    )

class Admin(models.Model):
    def __str__(self):
        return self.eagle_id
    
    eagle_id = models.CharField(max_length=8)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length = 254)
    class_year = models.CharField(max_length=4) 

class Planner(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    


class Major(models.Model):
    title = models.CharField(max_length=4)
    mum_credits = models.IntegerField()
    def __str__(self):
        return self.title

class Minor(models.Model):
    title = models.CharField(max_length=4)
    mum_credits = models.IntegerField()
    def __str__(self):
        return self.title

class Course(models.Model):
    class_code = models.CharField(max_length=4)
    associated_majors = models.ManyToManyField(Major)
    associated_minors = models.ManyToManyField(Minor)
    mum_credits = models.IntegerField()
    def __str__(self):
        return self.class_code

