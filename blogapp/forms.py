from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        fields = '__all__' 
        model = Blog