from django import forms
from .models import Comment


# Form

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', 'author')
