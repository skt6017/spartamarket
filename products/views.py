from django.shortcuts import render, redirect
from .forms import ProductForm

# Create your views here.

def index(request):
    return render(request, 'products/index.html')

def product_create(request):
    if request.method == "POST":
        # POST 요청 시, 폼 데이터를 포함한 ProductForm을 생성
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():  # 폼이 유효한지 검사
            form.save()  # 유효하면 데이터베이스에 저장
            # 리다이렉트 
    else:
        # GET 요청 시, 빈 ProductForm을 생성
        form = ProductForm()

    # 폼을 컨텍스트에 담아 템플릿으로 렌더링
    context = {"form": form}
    return render(request, "products/products_create.html", context)
