from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = (
        ('STUDENT', 'Student'),
        ('ADVISOR', 'Advisor'),
    )
    role = models.CharField(max_length=7, choices=ROLES, default='STUDENT')
    email = models.EmailField(max_length=254, unique=True)
    registered = models.BooleanField(default=False)


class Subject(models.Model):
    id = models.CharField(primary_key=True, max_length=4)
    short_name = models.CharField(max_length=100)
    long_name = models.CharField(max_length=200)

    def __str__(self):
        return self.long_name

class Course(models.Model):
    id = models.CharField(primary_key=True, max_length=8)
    title = models.CharField(max_length=100)
    subject_area = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
    
    class Meta:
        db_table = 'planner_course'
        
    def __str__(self):
        return self.title


class Major(models.Model):
    title = models.CharField(max_length=4)
    num_credits = models.IntegerField()
    def __str__(self):
        return self.title

class Minor(models.Model):
    title = models.CharField(max_length=4)
    num_credits = models.IntegerField()
    def __str__(self):
        return self.title
    
class Advisor(models.Model):
    def __str__(self):
        return self.first_name + " " + self.last_name
      
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, related_name="advisor")
    eagle_id = models.CharField(max_length=8)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length = 254)
    class_year = models.CharField(max_length=4) 

class Student(models.Model):
    def __str__(self):
        return self.first_name + " " + self.last_name
      
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, related_name="student")
    eagle_id = models.CharField(max_length=8)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=254, primary_key=True)
    advisor = models.ForeignKey(Advisor, default=None, on_delete=models.CASCADE, null=True)
    class_year = models.CharField(max_length=4)
    SEMESTER_CHOICES = (
        ('Spring', 'Spring'),
        ('Fall', 'Fall'),
    )
    end_semester = models.CharField(max_length=6, choices=SEMESTER_CHOICES, default='Spring')
    major_one = models.ForeignKey(Subject, default=None, on_delete=models.CASCADE, related_name="major_one")
    major_two = models.ForeignKey(Subject, default=None, on_delete=models.CASCADE, related_name="major_two", null=True)
    minor_one = models.ForeignKey(Subject, default=None, on_delete=models.CASCADE, related_name="minor_one", null=True)
    minor_two = models.ForeignKey(Subject, default=None, on_delete=models.CASCADE, related_name="minor_two", null=True)

    class College(models.TextChoices):
        MCAS = "MCAS", _("Morrissey College of Arts and Sciences")
        CSOM = "CSOM", _("Carroll School of Management")
        CSON = "CSON", _("William F. Connell School of Nursing")
        LYNCH = "LYNCH", _("Carolyn A. and Peter S. Lynch School of Education and Human Development")
    
    college = models.CharField(
        max_length=5,
        choices=College,
    )

class Semester(models.Model):
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(credit_hours__lte=21),
                name='credit_hours_limit'
            )
        ]

    credit_hours = models.PositiveIntegerField(default=0)
    courses = models.ManyToManyField(Course)
    

class Planner(models.Model):
    student = models.ForeignKey(Student, default=None, on_delete=models.CASCADE)
    fall_one = models.ForeignKey(Semester, default=None,on_delete=models.CASCADE, related_name='planner_sem_one')
    spring_one = models.ForeignKey(Semester,default=None, on_delete=models.CASCADE, related_name='planner_sem_two')
    fall_two = models.ForeignKey(Semester,default=None, on_delete=models.CASCADE, related_name='planner_sem_three')
    spring_two = models.ForeignKey(Semester,default=None, on_delete=models.CASCADE, related_name='planner_sem_four')
    fall_three = models.ForeignKey(Semester,default=None, on_delete=models.CASCADE, related_name='planner_sem_five')
    spring_three = models.ForeignKey(Semester, default=None,on_delete=models.CASCADE, related_name='planner_sem_six')
    fall_four = models.ForeignKey(Semester, default=None,on_delete=models.CASCADE, related_name='planner_sem_seven')
    spring_four = models.ForeignKey(Semester, default=None,on_delete=models.CASCADE, related_name='planner_sem_eight')
