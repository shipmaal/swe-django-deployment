import datetime
from django import forms
from planner.models import Planner, Semester, Course

class SemesterForm(forms.Form):
    class_one = forms.ModelChoiceField(
                    queryset=Course.objects.all(),
                    empty_label="Select Course",
                    required=True)
    class_two = forms.ModelChoiceField(
                    queryset=Course.objects.all(),
                    empty_label="Select Course",
                    required=True)
    class_three = forms.ModelChoiceField(
                    queryset=Course.objects.all(),
                    empty_label="Select Course",
                    required=True)
    class_four = forms.ModelChoiceField(
                    queryset=Course.objects.all(),
                    empty_label="Select Course",
                    required=True)
    class_five = forms.ModelChoiceField(
                    queryset=Course.objects.all(),
                    empty_label="Select Course",
                    required=False)
    class_siz = forms.ModelChoiceField(
                    queryset=Course.objects.all(),
                    empty_label="Select Course",
                    required=False)
    