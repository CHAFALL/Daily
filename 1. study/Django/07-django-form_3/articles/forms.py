from django import forms
from .models import Article
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    # 단, 추가적으로 뭔가를 할려면 써줘야 된다.
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title'
            }
        )
    )
# 클래스 쓰기 복잡해졌지만 유효성 검사와 기타 데이터 처리를 얻었다.



    # model 등록(위처럼 다시 쓸 필요 x)
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('title',)
        # exclude = ('title',)