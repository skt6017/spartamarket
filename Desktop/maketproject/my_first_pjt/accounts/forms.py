from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

User = get_user_model()
class CustomUserChangeForm(UserChangeForm):
    # password = None
    image = forms.ImageField(required=False, label="프로필 사진")

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'date_joined','image']  # 기본 User 모델 필드만 포함

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_joined'].label = "가입일자"
        #도움말 삭제
        self.fields['username'].help_text = None
        # Hide the password field
        self.fields['password'].widget = forms.HiddenInput()

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class CustomUserCreateForm(UserCreationForm):
    # 원래 있던 것은 그대로 사용
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def clean_password(self):
    # # always return the initial value
    #     return self.initial['password']
    
    # 보여주고 싶은것들만 표시
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email' ]
