import django.forms as forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateUserFormLanding(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class WriteForm(ModelForm):
    class Meta:
        model = Story
        fields = '__all__'
        exclude = ["user", "likes"]
    def __init__(self, *args, **kwargs):
        super(WriteForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'form-control'})
        self.fields['story'].widget.attrs.update({'class' : 'form-control', 'minlength' : '200'})
        self.fields['genre'].widget.attrs.update({'class' : 'form-control'})

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ["user", "story"]
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({'name' : 'comment'})