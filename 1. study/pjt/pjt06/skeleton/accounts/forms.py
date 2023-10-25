from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

# model 선택 3가지 방법

# 1. 직접 가져오기 -> 권장 x
# from .models import User

# 2. setting에 설정된 모델 가져오기 -> 문자열처럼 활용을 해야하는 경우에 이용, 즉, model.py에 작성할 때 이용
# from django.conf import settings 
# model = settings.AUTH_USER_MODEL

# 3. get_user_model메서드 활용
# from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        
        
