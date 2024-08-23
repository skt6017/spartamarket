
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Hashtag, Product
from django.db.models import Q

# Create your views here.


def index(request):
    return render(request, 'products/index.html')


def products(request):
    products = Product.objects.all().order_by("-pk")
    context = {"products": products}
    return render(request, "products/products.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.view_count += 1  # 조회수 기능(방문할때마다 +1)
    product.save()
    context = {'product': product}
    return render(request, "products/detail.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.view_count = 0
            product.save()
            form.save_m2m()  # m2m을 먼저 저장, 제품과 해시태그의 관계를 처리 준비
            # 사용자 입력한 new_hashtags필드가져옴, 기본은 ''
            new_hashtags = request.POST.get('new_hashtags', '')
            hashtags = [tag.strip('#')
                        for tag in new_hashtags.split() if tag.startswith('#')]
            # 문자열을 공백으로 분리, strip('#')를 통해 '#'를 제거, hashtags list로 변환
            for tag in hashtags:  # for each hashtag in hashtags
                if tag:  # if tag is not empty
                    hashtag, created = Hashtag.objects.get_or_create(
                        content=tag)  # hashtag object or create it
                    # add hashtag to product's hashtags
                    product.hashtags.add(hashtag)
            # redirect to product detail page
            return redirect('products:detail', pk=product.pk)
    else:
        form = ProductForm()
    # 폼을 컨텍스트에 담아 템플릿으로 렌더링
    context = {"form": form}
    return render(request, "products/create.html", context)


@require_http_methods(["GET", "POST"])
def update(request, pk):
    # pk를 기반, Product 객체를 가져오고, 없으면 404
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
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


@require_POST
def like(request, pk):
    if request.user.is_authenticated():
        product = get_object_or_404(Product, pk=pk)
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


def search(request):
    products = Product.objects.all().order_by('-id')
    # form 필드 'searched'가 POST 요청에 없다면 (검생창으로 받은 입력이 없음) 빈 문자열을 반환
    searched = request.POST.get('searched', '')

    # 검색값이 있다면(빈 문자열이 아니라면)
    if searched:
        # content가 검색값과 일치하는 hashtag들을 찾아내고 hashtag queryset을 저장함
        matching_hashtags = Hashtag.objects.filter(content__icontains=searched)

        # products에서 filter해 title,content, username, matching_hashtags에 검색값과 일치하는 값이 있는지 찾음
        products = products.filter(
            Q(title__icontains=searched) |
            Q(content__icontains=searched) |
            # ForeignKey인 author에는 icontains lookup을 사용할 수 없기 때문에 author의 username 필드에서 필터링
            Q(author__username__icontains=searched) |
            # product의 hashtags가 matching_hashtags에 있는지
            Q(hashtags__in=matching_hashtags)
        )
        context = {
            'products': products,
            'searched': searched,
        }
        return render(request, 'products/search.html', context)
    else:
        return render(request, 'products/search.html')
