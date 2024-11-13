from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['article', 'writer', 'comment']
        widgets = {
            'article': forms.HiddenInput(),
            'writer': forms.HiddenInput(),
        }