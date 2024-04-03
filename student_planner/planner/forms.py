import datetime
from django import forms
from planner.models import Planner, Semester, Course

class SemesterForm(forms.ModelForm):
    class Meta:
        model = Planner
        fields = [
            'id',
            'student',
            'fall_one',
            'spring_one',
            'fall_two',
            'spring_two',
            'fall_three',
            'spring_three',
            'fall_four',
            'spring_four',
        ]
        widgets = {
            '''
            'eagle_id': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'class_year': forms.Select(choices=year_choices, attrs={'class': 'form-control'}),
            'end_semester': forms.Select(attrs={'class': 'form-control'}),
            'college': forms.Select(attrs={'class': 'form-control'}),
            'advisor': forms.HiddenInput(),
            'advisor': forms.Select(attrs={'class': 'form-control'}),
            'major_one': forms.Select(attrs={'class': 'form-control'}),
            'major_two': forms.Select(attrs={'class': 'form-control'}),
            'minor_one': forms.Select(attrs={'class': 'form-control'}),
            'minor_two': forms.Select(attrs={'class': 'form-control'}),
            '''
            'id': forms.HiddenInput(),
            'student': forms.HiddenInput(),
            'fall_one':
            'spring_one',
            'fall_two',
            'spring_two',
            'fall_three',
            'spring_three',
            'fall_four',
            'spring_four',
        }
    major_one = forms.ModelChoiceField(queryset=Subject.objects.all(), 
                                       empty_label="Select a Major", 
                                       required=True)
    major_two = forms.ModelChoiceField(queryset=Subject.objects.all(), 
                                       empty_label="Select a Major", 
                                       required=False)
    minor_one = forms.ModelChoiceField(queryset=Subject.objects.all(),
                                        empty_label="Select a Minor",
                                        required=False)
    minor_two = forms.ModelChoiceField(queryset=Subject.objects.all(),
                                        empty_label="Select a Minor",
                                        required=False)

    