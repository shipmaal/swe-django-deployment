import datetime
from django import forms
from planner.models import Student, Major, Minor

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
            'major_one',
            'major_two',
            'minor_one',
            'minor_two',
        ]
        widgets = {
            'eagle_id': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'class_year': forms.Select(choices=year_choices, attrs={'class': 'form-control'}),
            'end_semester': forms.Select(attrs={'class': 'form-control'}),
            'college': forms.Select(attrs={'class': 'form-control'}),
            'major_one': forms.Select(attrs={'class': 'form-control'}),
            'major_two': forms.Select(attrs={'class': 'form-control'}),
            'minor_one': forms.Select(attrs={'class': 'form-control'}),
            'minor_two': forms.Select(attrs={'class': 'form-control'}),
        }
    major_one = forms.ModelChoiceField(queryset=Major.objects.all(), 
                                       empty_label="Select a Major", 
                                       required=False)

    major_two = forms.ModelChoiceField(queryset=Major.objects.all(), 
                                       empty_label="Select a Major", 
                                       required=False)
    minor_one = forms.ModelChoiceField(queryset=Minor.objects.all(),
                                        empty_label="Select a Minor",
                                        required=False)
    minor_two = forms.ModelChoiceField(queryset=Minor.objects.all(),
                                        empty_label="Select a Minor",
                                        required=False)

        
