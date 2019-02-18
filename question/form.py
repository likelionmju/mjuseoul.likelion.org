from django import forms
from .models import Question, Comment

class QuestionPost(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body', 'writer', 'password']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'writer', 'password']