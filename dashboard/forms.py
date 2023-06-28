from django import forms
from . models import *


class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title','description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }



class HomeworkForm(forms.ModelForm):
    class Meta:
        model=Homework
        fields=['subject','title','description','due','is_finished']

        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'due': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            # 'is_finished': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user', None)
    #     super().__init__(*args, **kwargs)
    #     if user:
    #         self.fields['user'].initial = user
    
    # user = forms.CharField(widget=forms.HiddenInput())
        
class Dashboardform(forms.Form):
    text=forms.CharField(max_length=100,label="Enter your search  ")