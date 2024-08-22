from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import ProductForm
from .models import Product

# Create your views here.

def index(request):
    return render(request, 'products/index.html')

@login_required
def product_create(request):
    if request.method == "POST":
        # POST 요청 시, 폼 데이터를 포함한 ProductForm을 생성
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():  # 폼이 유효한지 검사
            form.instance.author = request.user #author로그인 지정
            form.save()  # 유효하면 데이터베이스에 저장
            return redirect('products:product_detail', pk=form.instance.pk)  # 저장한 product
    else:
        # GET 요청 시, 빈 ProductForm을 생성
        form = ProductForm()

    # 폼을 컨텍스트에 담아 템플릿으로 렌더링
    context = {"form": form}
    return render(request, "products/product_create.html", context)

def product_update(request, pk):
    # pk를 기반, Product 객체를 가져오고, 없으면 404
    product = get_object_or_404(Product, pk=pk)
    
    # 요청이 POST인 경우, 
    if request.method == 'POST':
        # POST 데이터를 기반으로 기존 product 인스턴스를 업데이트하기 위해 폼을 초기화
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            # 유효성 검사를 통과하면 폼 데이터 저장
            form.save()
            # 상품 상세 페이지로 리다이렉트
            return redirect('products:product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    
    # 폼과 product 데이터를 컨텍스트에 담아 템플릿에 전달
    return render(request, 'products/product_update.html', {'form': form, 'product': product})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        product.delete()
        return redirect('index')
    
    return render(request, 'products/product_delete.html', {'product': product})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.view_count += 1
    product.save()
    return render(request, 'products/product_detail.html', {'product': product})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
