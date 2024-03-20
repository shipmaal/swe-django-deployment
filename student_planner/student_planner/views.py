from django.views import generic
from .forms import StudentForm
from django.views.generic.edit import FormView
from planner.models import Student


class StudentInfoView(generic.UpdateView):
    form_class = StudentForm
    template_name = 'student_info.html'
    success_url = '/'

    def get_object(self):
        return self.request.user
    
class LoginView(FormView):
    form_class = StudentForm
    template_name = 'index.html'
    success_url = '/'

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user
        else:
        # Handle the case where the user is not authenticated
            return None

    def form_valid(self, form):
        # Set user.registered to True
        self.request.user.registered = True
        self.request.user.save()

        # Create a new student
        student = Student(
            user=self.request.user,
            eagle_id=form.cleaned_data['eagle_id'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            email=form.cleaned_data['email'],
            class_year=form.cleaned_data['class_year'],
            end_semester=form.cleaned_data['end_semester'],
            major_one=form.cleaned_data['major_one'],
            major_two=form.cleaned_data['major_two'],
            minor_one=form.cleaned_data['minor_one'],
            minor_two=form.cleaned_data['minor_two'],
        )
        student.save()

        return super().form_valid(form)

    def get_initial(self):
        if not self.request.user.is_authenticated:
            return {}
        
        initial = super().get_initial()

        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        initial['email'] = self.request.user.email

        return initial
