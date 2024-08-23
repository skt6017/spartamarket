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
            form.save_m2m()
            new_hashtags = request.POST.get('new_hashtags', '').split(',')
            for tag in new_hashtags:
                if tag.strip():
                    hashtag, created = Hashtag.objects.get_or_create(content=tag.strip())
                    product.hashtags.add(hashtag)
            return redirect('products:detail', pk=product.pk) 
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
        return redirect('index')
    
    return render(request, 'products/products.html', {'product': product})


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