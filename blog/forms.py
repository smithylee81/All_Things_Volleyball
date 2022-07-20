from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author','content', 'status']

class CommentForm(forms.ModelForm):
       """ Create comment form for blog posts """
class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

