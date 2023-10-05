from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea) # 여기가 조금 다름(form에서는 TextField가 없음)
#     # widget은 input의 표현만 바꿀 뿐인 기능


# 중복 줄일려고 이용
# 이미 모델이 어떤 필드를 가지고 있는지 알고있기 때문에 model 등록만 하면 됨
class ArticleForm(forms.ModelForm):
    # 위젯(커스텀)을 쓸려면 아래처럼 재정의를 해줘야 됨
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            # 부트스트랩 클래스 사용가능하겠지??(전보다 불편?? 하지만 유효성 검사나 그런 것들은 얻음 기브엔 테이크)
            attrs={
                'class': 'my-title'
            }
        )
    )

    # model 등록
    class Meta:
        model = Article
        fields = '__all__' # 전체 필드를 선택해주는 옵션(렌더링 검사를 통해 알아서 골라줌)
        # fields = ('title',) # 내가 출력하고자 하는 필드 지정하는 방식
        # exclude = ('title',) # 내가 출력하지 않고자하는 필드 지정

    # 메타데이터란? 어떠한 데이터에 대한 데이터임
    # 그래서 이 Article에 대한 데이터라서 Meta라고 그냥 쓰인것임

#참고: created_at과 updated_at 은 사용자로 부터 받아지는 것이 아니라서 렌더링 해석과정에서 필요없다고 판단 됨