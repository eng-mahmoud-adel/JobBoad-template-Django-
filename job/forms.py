from django import forms
from .models import ApplyForJob, Job

class ApplyForJobForm(forms.ModelForm):
    class Meta:
        model = ApplyForJob
        fields = ['name', 'email', 'website', 'cv', 'cover_letter']

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('owner', 'slug')
 