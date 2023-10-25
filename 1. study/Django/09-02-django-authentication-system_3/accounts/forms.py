from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

# 상속을 누구를 받겠다?? 지금 현재 문제가 있는 UserCreationForm을 받겠다. 거기서 클래스 Meta부분만 오버라이딩을 하겠다.
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 왜 직접 참조를 하지 않고 이렇게 약간 간접적으로 본인들이 만들어 놓은 함수를 사용하게 할까??
        # 유지보수 GOOD
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')
