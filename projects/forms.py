from django import forms
from . import models

attrs = {'class': 'form-control'}

class ProjectCreatForm(forms.ModelForm):
   
   #Metadata
   class Meta:
       model = models.Project
       fields = ['category', 'title', 'description']
       widgets = {
           'category': forms.Select(attrs=attrs),
           'title': forms.TextInput(attrs=attrs),
           'description' : forms.Textarea(attrs=attrs),
           
       }


class ProjectUpdateForm(forms.ModelForm):
   
   #Metadata
   class Meta:
       model = models.Project
       fields = ['category', 'title', 'status']
       widgets = {
           'category': forms.Select(attrs=attrs),
           'title': forms.TextInput(attrs=attrs),
           'status' : forms.Select(attrs=attrs),
           
       }


