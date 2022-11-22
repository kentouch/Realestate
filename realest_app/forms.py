from django import forms
from .models import Testimony

# creating a form

class CommentForm(forms.ModelForm):

        comment = forms.CharField(label = "", widget= forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder': 'Leave your comment..',
                'rows':5,
                'cols':5
            }
        ))

        class Meta:

            model = Testimony
            fields = ['comment']

       