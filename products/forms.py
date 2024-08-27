
import re
from django import forms
from .models import Product, Hashtag

class ProductForm(forms.ModelForm):
    hashtags = forms.ModelMultipleChoiceField(
        queryset=Hashtag.objects.all(), # hashtags queryset
        widget=forms.HiddenInput,
        required=False #필수선택아님
    )

    class Meta:
        model = Product  
        fields = "__all__"
        exclude = ["author","like_users","view_count", "hashtags",]

    def clean(self):
        cleaned_data = super().clean()
        new_hashtags = cleaned_data.get('new_hashtags')

        # 해시태그 검증 로직
        if new_hashtags:
            hashtags = new_hashtags.split()
            for tag in hashtags:
                if re.search(r'[^a-zA-Z0-9가-힣]', tag):
                    raise forms.ValidationError("해시태그는 띄어쓰기와 특수문자가 허용되지 않습니다.")
        
        return cleaned_data