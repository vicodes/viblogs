from django import forms
from . import models


class CreateArticle(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': "materialize-textarea"}))
    class Meta:
        model = models.Post
        fields = ['title','body']
