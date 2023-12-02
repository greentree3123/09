from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'sales', 'place', 'account', 'content']

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')