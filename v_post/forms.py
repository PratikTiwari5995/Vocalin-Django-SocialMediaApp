from .models import *
from django.forms import ModelForm
from django import forms


class PostCreateForms(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'photo', 'body', 'tags']
        lables = {
            'body': 'Caption',
            'tags': 'category'
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add the caption...', 'class': 'font1 text-4xl'}),
            'tags': forms.CheckboxSelectMultiple()
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'photo', 'body', 'tags']

        labels = {
            'title': 'Post Title',
            'photo': 'Upload Image',
            'body': 'Post Content',
            'tags': 'category'
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title'
            }),
            'photo': forms.FileInput(),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type your content here...',
                'rows': 6
            }),
            'tags': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(EditPostForm, self).__init__(*args, **kwargs)
        self.fields['photo'].widget.initial_text = ''
        self.fields['photo'].widget.input_text = ''
        self.fields['photo'].widget.clear_checkbox_label = ''
