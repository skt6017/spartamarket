from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProductForm
from .models import Product
from django.views.decorators.http import require_http_methods, require_POST

# Create your views here.

def products(request):
    products = Product.objects.all().order_by("-pk")
    context = {"products": products}
    return render(request, "products/products.html", context)

def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product':product}
    return render(request, "products/detail.html", context)

def product_create(request):
    if request.method == "POST":
        # POST 요청 시, 폼 데이터를 포함한 ProductForm을 생성
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():  # 폼이 유효한지 검사
            product = form.save(commit = False)  # 유효하면 데이터베이스에 저장
            product.author = request.user       # Set additional fields
            product.save()  
            # 리다이렉트 
            return redirect('products:detail', product.pk)
    else:
        # GET 요청 시, 빈 ProductForm을 생성
        form = ProductForm()

    # 폼을 컨텍스트에 담아 템플릿으로 렌더링
    context = {"form": form}
    return render(request, "products/products_create.html", context)


@require_POST
def like(request, product_pk):
    if request.user.is_authenticated():
        product = get_object_or_404(Product, pk = product_pk)
        # request.user가 상품을 이미 좋아요 한 상태이면 좋아요한 유저에서 delete
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.delete(request.user)
        else:
            product.like_users.add(request.user)
        # products 페이지로 리다이렉트
        return redirect('products:products')
    # 로그인 되어있지 않으면 로그인 페이지로 리다이렉트
    return redirect('accounts:login')

    
