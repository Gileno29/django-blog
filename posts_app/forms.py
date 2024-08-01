from django import forms

from .models import Posts


# classe para definir o models do django como um formulario
class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'description', 'image'] 

