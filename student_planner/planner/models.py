import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


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
    
    eagle_id = models.CharField(max_length=8)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length = 254)
    class_year = models.CharField(max_length=4)
    end_semester = models.CharField(max_length=6, default="Spring")

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
    


class Program(models.Model):
    title = models.CharField(max_length=4)
    mum_credits = models.IntegerField()
    def __str__(self):
        return self.title

class Course(models.Model):
    class_code = models.CharField(max_length=4)
    associated_programs = models.ManyToManyField(Program)
    mum_credits = models.IntegerField()
    def __str__(self):
        return self.class_code