from dataclasses import field
from email.policy import default
import re
from turtle import title
from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    title = forms.CharField(required=False)

    class Meta:
        model = Note
        fields = ('title', 'content')
