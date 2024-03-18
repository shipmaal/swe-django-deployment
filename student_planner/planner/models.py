import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField


''' Example Models:
# Create your models here.
class Question(models.Model):
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) 
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
'''

class Student(models.Model):
    def __str__(self):
        return self.eagle_id
    eagle_id = models.IntegerField(max_length=8,primary_key)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length = 254)
    class_year = models.IntegerField(max_length=4)

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


class Planner(models.Model):


class Program(models.Model):

'''
class Course(models.Model):
    school =
    department = 
    course_name =
    course_number =
    cedits =

    class CourseLevel(models.TextChoices):
        UNDERGRAD
        GRAD
    course_level = MultiSelectField(choices=CourseLevel)

    class FulfilledReq(models.TextChoices):
'''
