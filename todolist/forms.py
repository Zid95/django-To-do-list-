from django import forms
from .models import *


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todo', 'check_todo', 'datetime']

        labels = {
            "todo": "",
        }

        widgets = {
            'todo': forms.TextInput(attrs={'class': 'form-control fs-5'}),
            'check_todo': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'datetime': forms.DateInput(attrs={'class': 'form-control mt-3 ',
                                               'placeholder': 'Select a date',
                                               'type': 'date'}),
        }
