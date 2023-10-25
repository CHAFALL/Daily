from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    content = forms.CharField(
        label='Description',
        widget=forms.Textarea(
            attrs={
                'rows':10,
                'cols':40,
            }
        )
    )

    class Meta:
        model = Movie
        fields = '__all__'
