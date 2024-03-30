import datetime
from django import forms
from planner.models import Student, Major, Minor, Advisor

year_choices = [(r,r) for r in range(2025, datetime.date.today().year+4)]
current_year = datetime.date.today().year

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'eagle_id',
            'first_name',
            'last_name',
            'email',
            'class_year',
            'end_semester',
            'college',
            'advisor',
            'major_one',
            'major_two',
            'minor_one',
            'minor_two',
        ]
        widgets = {
            'eagle_id': forms.TextInput(attrs={'class': 'form-control',}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'class_year': forms.Select(choices=year_choices, attrs={'class': 'form-control'}),
            'end_semester': forms.Select(attrs={'class': 'form-control'}),
            'college': forms.Select(attrs={'class': 'form-control'}),
            'advisor': forms.HiddenInput(),
            'major_one': forms.Select(attrs={'class': 'form-control'}),
            'major_two': forms.Select(attrs={'class': 'form-control'}),
            'minor_one': forms.Select(attrs={'class': 'form-control'}),
            'minor_two': forms.Select(attrs={'class': 'form-control'}),
        }
    major_one = forms.ModelChoiceField(queryset=Major.objects.all(), 
                                       empty_label="Select a Major", 
                                       required=True)
    major_two = forms.ModelChoiceField(queryset=Major.objects.all(), 
                                       empty_label="Select a Major", 
                                       required=False)
    minor_one = forms.ModelChoiceField(queryset=Minor.objects.all(),
                                        empty_label="Select a Minor",
                                        required=False)
    minor_two = forms.ModelChoiceField(queryset=Minor.objects.all(),
                                        empty_label="Select a Minor",
                                        required=False)

class StudentAccountForm(StudentForm):
    class Meta(StudentForm.Meta):
        fields = StudentForm.Meta.fields + ['advisor']
        widgets = {**StudentForm.Meta.widgets, 
                   'advisor': forms.Select(attrs={'class': 'form-control'}),
                   'eagle_id': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'})}
        advisor = forms.ModelChoiceField(queryset=Advisor.objects.all(),
                                        empty_label="Select an Advisor",
                                        required=False)
                                        

class StudentRegisterForm(StudentForm):
    class Meta(StudentForm.Meta):
        fields = StudentForm.Meta.fields
        widgets = {**StudentForm.Meta.widgets}
    