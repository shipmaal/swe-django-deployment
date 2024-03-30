import datetime
from django import forms
from planner.models import Student, Major, Minor, Advisor

year_choices = [(r,r) for r in range(2025, datetime.date.today().year+4)]
current_year = datetime.date.today().year

def create_widget(field_type, **kwargs):
    attrs = {'class': 'form-control'}
    if kwargs.get('disabled'):
        attrs['disabled'] = 'disabled'
    if field_type == 'TextInput':
        return forms.TextInput(attrs=attrs)
    elif field_type == 'EmailInput':
        return forms.EmailInput(attrs=attrs)
    elif field_type == 'Select':
        return forms.Select(choices=kwargs.get('choices', []), attrs=attrs)
    elif field_type == 'HiddenInput':
        return forms.HiddenInput()
    else:
        return None

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
            'eagle_id': create_widget('TextInput'),
            'first_name': create_widget('TextInput', disabled=True),
            'last_name': create_widget('TextInput', disabled=True),
            'email': create_widget('EmailInput', disabled=True),
            'class_year': create_widget('Select', choices=year_choices),
            'end_semester': create_widget('Select'),
            'college': create_widget('Select'),
            'advisor': create_widget('HiddenInput'),
            'major_one': create_widget('Select'),
            'major_two': create_widget('Select'),
            'minor_one': create_widget('Select'),
            'minor_two': create_widget('Select'),
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
        fields = StudentForm.Meta.fields
        widgets = {**StudentForm.Meta.widgets, 
                   'advisor': create_widget('Select', choices=[]),
                   'eagle_id': create_widget('TextInput', disabled=True),}
        advisor = forms.ModelChoiceField(queryset=Advisor.objects.all(),
                                        empty_label="Select an Advisor",
                                        required=False)
                                        

class StudentRegisterForm(StudentForm):
    class Meta(StudentForm.Meta):
        fields = StudentForm.Meta.fields
        widgets = {**StudentForm.Meta.widgets}
    