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


class Course(models.Model):
    course_code = models.CharField(max_length=8, db_column='courseCode', null = True) #renamed from class_code
    course_title = models.CharField(max_length=50, default="", db_column='title') #renamed from class_name
    course_description = models.CharField(max_length=200, default="") #renamed from class_description
    course_level = models.CharField(max_length=10, default="Undergraduate")
    course_semester = models.CharField(max_length=15, default="Every semester") #this may need to be changed to offering enablers
    course_prerequisites = models.ManyToManyField('self', symmetrical=False, related_name='required_by', blank=True)
    course_corequisites = models.ManyToManyField('self', symmetrical=False, related_name='required_with', blank=True)
    associated_majors = models.ManyToManyField(Major)
    associated_minors = models.ManyToManyField(Minor)
    num_credits = models.IntegerField()
    subject_area = models.CharField(max_length=4, db_column='subjectApiId', null = True)
    #deleted class prof, class time, class days, class location

    class Meta:
        db_table = 'planner_course'
    def __str__(self):
        return self.class_code


class Semester(models.Model):
    class_one = models.ForeignKey(Course, default=None, on_delete=models.CASCADE, related_name='class_one')
    class_two = models.ForeignKey(Course, default=None, on_delete=models.CASCADE, related_name='class_two')
    class_three = models.ForeignKey(Course, default=None, on_delete=models.CASCADE, related_name='class_three')
    class_four = models.ForeignKey(Course, default=None, on_delete=models.CASCADE, related_name='class_four')
    class_five = models.ForeignKey(Course, default=None, on_delete=models.CASCADE, related_name='class_five')
    class_six = models.ForeignKey(Course, default=None, on_delete=models.CASCADE, related_name='class_six')


class Planner(models.Model):
    student = models.ForeignKey(Student, default=None, on_delete=models.CASCADE)
    sem_one = models.ForeignKey(Semester, default=None,on_delete=models.CASCADE, related_name='planner_sem_one')
    sem_two = models.ForeignKey(Semester,default=None, on_delete=models.CASCADE, related_name='planner_sem_two')
    sem_three = models.ForeignKey(Semester,default=None, on_delete=models.CASCADE, related_name='planner_sem_three')
    sem_four = models.ForeignKey(Semester,default=None, on_delete=models.CASCADE, related_name='planner_sem_four')
    sem_five = models.ForeignKey(Semester,default=None, on_delete=models.CASCADE, related_name='planner_sem_five')
    sem_six = models.ForeignKey(Semester, default=None,on_delete=models.CASCADE, related_name='planner_sem_six')
    sem_seven = models.ForeignKey(Semester, default=None,on_delete=models.CASCADE, related_name='planner_sem_seven')
    sem_eight = models.ForeignKey(Semester, default=None,on_delete=models.CASCADE, related_name='planner_sem_eight')




