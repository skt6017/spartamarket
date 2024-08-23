
from django import forms
from .models import Product

# ProductForm: Product 모델의 form
class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product  
        fields = "__all__"
        exclude = ["author","view_count"]