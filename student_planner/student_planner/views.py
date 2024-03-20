from django.views import generic
from .forms import StudentAccountForm, StudentLoginForm
from django.views.generic.edit import FormView, UpdateView
from planner.models import Student


class AccountView(UpdateView):
    form_class = StudentAccountForm
    template_name = 'account.html'
    success_url = '/'

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user
        else:
        # Handle the case where the user is not authenticated
            return None

    def form_valid(self, form):
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
            college=form.cleaned_data['college'],
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
        
        student = self.request.user.student
        
        initial = super().get_initial()

        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        initial['email'] = self.request.user.email
        initial['eagle_id'] = student.eagle_id
        initial['class_year'] = student.class_year
        initial['end_semester'] = student.end_semester
        initial['college'] = student.college
        initial['major_one'] = student.major_one
        initial['major_two'] = student.major_two
        initial['minor_one'] = student.minor_one
        initial['minor_two'] = student.minor_two


        return initial

    
class LoginView(FormView):
    form_class = StudentLoginForm
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
