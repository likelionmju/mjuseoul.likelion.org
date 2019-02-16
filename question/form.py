from django import forms
from .models import Question

class QuestionPost(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body', 'writer', 'password']