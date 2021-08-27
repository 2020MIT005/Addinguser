from django import forms

from .models import Project

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name','image1','image2','image3')
        # widgets = {
        #   'text': forms.Textarea(attrs={'rows':3, 'cols':25}),
        # }