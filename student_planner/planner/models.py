from django.db import models
from django.utils.translation import gettext_lazy as _

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
        return self.eagle_id
    
    eagle_id = models.CharField(max_length=8)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length = 254)
    class_year = models.CharField(max_length=4) 

class Student(models.Model):
    def __str__(self):
        return self.eagle_id
    eagle_id = models.CharField(max_length=8)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=254, primary_key=True)
    advisor = models.ForeignKey(Advisor, default=None, on_delete=models.CASCADE)
    class_year = models.CharField(max_length=4)
    end_semester = models.CharField(max_length=6, default="Spring")
    major_one = models.ForeignKey(Major, default=None, on_delete=models.CASCADE, related_name="major_one")
    major_two = models.ForeignKey(Major, default=None, on_delete=models.CASCADE, related_name="major_two")
    minor_one = models.ForeignKey(Minor, default=None, on_delete=models.CASCADE, related_name="minor_one")
    minor_two = models.ForeignKey(Minor, default=None, on_delete=models.CASCADE, related_name="minor_two")

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
    associated_majors = models.ManyToManyField(Major)
    associated_minors = models.ManyToManyField(Minor)
    num_credits = models.IntegerField()
    def __str__(self):
        return self.class_code
