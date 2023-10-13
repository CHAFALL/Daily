from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'step' : 0.5,
                'max' : 5.0,
                'min' : 0.0,
            }
        ),
    )
    class Meta:
        model = Movie
        exclude = ('user',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
