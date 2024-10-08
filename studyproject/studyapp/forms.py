from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Study

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = ['study_name', 'study_description', 'study_phase', 'sponsor_name']
        widgets = {
            'study_name': forms.TextInput(attrs={'placeholder': 'Enter study name'}),
            'study_description': forms.Textarea(attrs={'placeholder': 'Enter study description'}),
            'study_phase': forms.Select(),
            'sponsor_name': forms.TextInput(attrs={'placeholder': 'Enter or select sponsor name'}),
        }
