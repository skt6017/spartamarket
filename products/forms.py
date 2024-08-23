
from django import forms
from .models import Product, Hashtag

class ProductForm(forms.ModelForm):
    hashtags = forms.ModelMultipleChoiceField(
        queryset=Hashtag.objects.all(), # hashtags queryset
        widget=forms.CheckboxSelectMultiple, #체크박스위젯을 제공선택가능
        required=False #필수선택아님
    )

    class Meta:
        model = Product  
        fields = "__all__"
        exclude = ["author","like_users","view_count"]