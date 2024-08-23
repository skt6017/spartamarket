
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from .forms import ProductForm
from .models import Hashtag, Product

def products(request):
    products = Product.objects.all().order_by("-pk")
    context = {"products": products}
    return render(request, "products/products.html", context)

def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product':product}
    return render(request, "products/detail.html", context)

def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            form.save_m2m() # m2m을 먼저 저장, 제품과 해시태그의 관계를 처리 준비
            new_hashtags = request.POST.get('new_hashtags', '') #사용자 입력한 new_hashtags필드가져옴, 기본은 ''
            hashtags = [tag.strip('#') for tag in new_hashtags.split() if tag.startswith('#')]
            #문자열을 공백으로 분리, strip('#')를 통해 '#'를 제거, hashtags list로 변환
            for tag in hashtags: #for each hashtag in hashtags
                if tag: # if tag is not empty
                    hashtag, created = Hashtag.objects.get_or_create(content=tag) # hashtag object or create it
                    product.hashtags.add(hashtag)  # add hashtag to product's hashtags
            return redirect('products:detail', pk=product.pk) # redirect to product detail page
    else:
        form = ProductForm()
    context = {"form": form}

    return render(request, "products/create.html", context)

def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'products/update.html', {'form': form, 'product': product})

def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        product.delete()
        return redirect('products:products')
    
    return redirect('index')


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

@login_required
def hashtag(request, hashtag_pk):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_pk)
    products = Product.objects.filter(hashtags=hashtag)
    context = {
        'hashtag': hashtag, 
        'products': products,
    }
    return render(request, 'products/hashtag.html', context)

    
def index(request):
    return render(request, 'products/index.html')