from django import forms
from . import models

class ProjectCreatForm(forms.ModelForm):
   
   #Metadata
   class Meta:
       model = models.Project
       fields = ['category', 'title', 'description']
       Widget = {
           'category': forms.Select(),
           'title': forms.TextInput(),
           'description' : forms.Textarea(),
           
       }
