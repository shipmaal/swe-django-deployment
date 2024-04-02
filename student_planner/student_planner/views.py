from django.views.generic import TemplateView
from .forms import StudentAccountForm, StudentRegisterForm
from django.views.generic.edit import FormView, UpdateView
from django.shortcuts import redirect
from planner.models import Student


class AccountView(UpdateView):
    form_class = StudentAccountForm
    template_name = 'account.html'
    success_url = '/'

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user
        else:
            return None

    def form_valid(self, form):
        self.request.user.save()
        student = Student(
            user=self.request.user,
            **form.cleaned_data
        )
        student.save()

        return super().form_valid(form)

    def get_initial(self):
        if not self.request.user.is_authenticated:
            return {}
        
        student = self.request.user.student
        initial = super().get_initial()
        user_fields = ['first_name', 'last_name', 'email']
        student_fields = ['eagle_id', 'class_year', 'end_semester', 'college', 'advisor', 'major_one', 'major_two', 'minor_one', 'minor_two']

        for field in user_fields:
            initial[field] = getattr(self.request.user, field)

        for field in student_fields:
            initial[field] = getattr(student, field)

        return initial

    
class LoginView(TemplateView):
    template_name = 'index.html'

    
class RegisterView(FormView):
    form_class = StudentRegisterForm
    template_name = 'register.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login/')
        
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user
        else:
            return None

    def form_valid(self, form):
        self.request.user.registered = True
        self.request.user.save()

        student = Student(user=self.request.user, **form.cleaned_data)
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
    