from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    summary = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'summary',
            }
        ),
    )
    memo = forms.CharField(
        widget=forms.Textarea(
            attrs = {
                'placeholder': 'Enter the content',
                'rows':5,
                'cols':50,
            }
        )
    )

    class Meta:
        model = Memo
        fields = '__all__'
