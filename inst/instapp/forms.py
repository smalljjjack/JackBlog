from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author', 'title', 'text')
        widgets = {
            'title':forms.TextInput(attrs = {'class':'textInputClass'}),
            'text':forms.Textarea(attrs = {'class':'editable medium-editor-textarea postcontent'})
            # both textInputClass postcontent are our own css classes, so have to selfwrite them
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author':forms.TextInput(attrs = {'class':'textInputClass'}),
            'text':forms.Textarea(attrs = {'class':'editable medium-editor-textarea postcontent'})
        }
