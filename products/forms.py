
from django import forms
from .models import Product, Hashtag

class ProductForm(forms.ModelForm):
    hashtags = forms.ModelMultipleChoiceField(
        queryset=Hashtag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Product  
        fields = "__all__"
        exclude = ("author", "view_count")