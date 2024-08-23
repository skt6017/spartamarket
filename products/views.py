from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product
# Create your views here.
def index(request):
    return render(request, 'products/index.html')

def products(request):
    products = Product.objects.all().order_by("-pk")
    context = {"products": products}
    return render(request, "products/products.html", context)

@login_required
@require_http_methods(["GET","POST"])
def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.view_count += 1 #조회수 기능(방문할때마다 +1)
    product.save()
    context = {'product':product}
    return render(request, "products/detail.html", context)

@login_required
@require_http_methods(["GET","POST"])
def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():  # 폼이 유효한지 검사
            product = form.save(commit=False)
            product.author = request.user # product author 입력
            product.view_count = 1 # product 생성시 view_count는 1로 초기화
            product.save()  # 유효하면 데이터베이스에 저장
        return redirect("products:detail", product.pk) 
    else:
        form = ProductForm()
    # 폼을 컨텍스트에 담아 템플릿으로 렌더링
    context = {"form": form}
    return render(request, "products/create.html", context)

@require_http_methods(["GET","POST"])
def update(request, pk):
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
            return redirect('products:detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    
    # 폼과 product 데이터를 컨텍스트에 담아 템플릿에 전달
    return render(request, 'products/update.html', {'form': form, 'product': product})

@login_required
@require_POST
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user == product.author:
        product.delete()
        return redirect('products:prodcuts')
    else:
        return redirect('prodcuts:detial', pk)
    

@login_required
@require_POST
def like(request, pk):
    if request.user.is_authenticated():
        product = get_object_or_404(Product, pk = pk)
        # request.user가 상품을 이미 좋아요 한 상태이면 좋아요한 유저에서 delete
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.delete(request.user)
        else:
            product.like_users.add(request.user)
        # products 페이지로 리다이렉트
        return redirect('products:products')
    # 로그인 되어있지 않으면 로그인 페이지로 리다이렉트
    return redirect('accounts:login')

    
