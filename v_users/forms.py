from .models import *
from django.forms import ModelForm
from django import forms


class EditPofileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

        labels = {
            'realname': 'Name'
        }

        widgets = {
            'avatar': forms.FileInput(),
            'bio': forms.Textarea(attrs={'rows': 3})
        }