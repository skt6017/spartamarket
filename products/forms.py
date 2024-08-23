
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