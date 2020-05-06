from django import forms
from django.utils.text import slugify
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """Класс формы комментариев"""
    class Meta:
        model = Comment
        fields = ("text", )


class PostForm(forms.ModelForm):
    """Класс формы для постов"""
    class Meta:
        model = Post
        fields = (slugify('title'), 'description', 'text', 'category')
