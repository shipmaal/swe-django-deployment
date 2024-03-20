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
    major_one = models.ForeignKey(Major, default=None, on_delete=models.CASCADE, related_name="major_one")
    major_two = models.ForeignKey(Major, default=None, on_delete=models.CASCADE, related_name="major_two", null=True)
    minor_one = models.ForeignKey(Minor, default=None, on_delete=models.CASCADE, related_name="minor_one", null=True)
    minor_two = models.ForeignKey(Minor, default=None, on_delete=models.CASCADE, related_name="minor_two", null=True)

    class College(models.TextChoices):
        MCAS = "MCAS", _("Morrissey College of Arts and Sciences")
        CSOM = "CSOM", _("Carroll School of Management")
        CSON = "CSON", _("William F. Connell School of Nursing")
        LYNCH = "LYNCH", _("Carolyn A. and Peter S. Lynch School of Education and Human Development")
    
    college = models.CharField(
        max_length=5,
        choices=College,
    )


class Planner(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Course(models.Model):
    class_code = models.CharField(max_length=4)
    class_name = models.CharField(max_length=50, default="")
    class_description = models.CharField(max_length=200, default="")
    class_location = models.CharField(max_length=50, default="")
    class_time = models.TimeField(default="00:00:00")
    class_days = models.CharField(max_length=10, default="MWF")
    class_semester = models.CharField(max_length=6, default="Spring")
    class_professor = models.CharField(max_length=50, default="Joe Smith")
    associated_majors = models.ManyToManyField(Major)
    associated_minors = models.ManyToManyField(Minor)
    num_credits = models.IntegerField()
    def __str__(self):
        return self.class_code
