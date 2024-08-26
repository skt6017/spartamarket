from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Hashtag, Product
from django.db.models import Q
import re

# Create your views here.

def index(request):
    return render(request, 'products/index.html')

def products(request):
    sort_by = request.GET.get('sort', '-view_count')
    products = Product.objects.all().order_by(sort_by)
    context = {
        "products": products,
        "sort_by": sort_by
        }
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
            
            # 사용자 입력한 new_hashtags 필드 가져옴, 기본은 ''
            new_hashtags = request.POST.get('new_hashtags', '')
            hashtags = [tag.strip('#') for tag in new_hashtags.split() if tag.startswith('#')]

            ### 해시태그 검증 로직 추가 ###
            valid_hashtags = []
            for tag in hashtags:
                if re.search(r'\s', tag):  # 공백이 포함되어 있는지 확인
                    form.add_error(None, f"해시태그 '{tag}'는 공백을 포함할 수 없습니다.")
                elif re.search(r'[^a-zA-Z0-9가-힣]', tag):  # 특수문자가 포함되어 있는지 확인
                    form.add_error(None, f"해시태그 '{tag}'는 특수문자를 포함할 수 없습니다.")
                else:
                    valid_hashtags.append(tag)
            
            if form.errors:  # 유효하지 않은 해시태그가 있을 경우, 폼을 다시 렌더링
                return render(request, "products/create.html", {"form": form})

            # 검증된 해시태그만 제품에 추가
            for tag in valid_hashtags:
                if tag:  # if tag is not empty
                    hashtag, created = Hashtag.objects.get_or_create(
                        content=tag)  # hashtag object or create it
                    # add hashtag to product's hashtags
                    product.hashtags.add(hashtag)
            # redirect to product detail page
            return redirect('products:detail', pk=product.pk)
    else:
        form = ProductForm()
    context = {"form": form}
    return render(request, "products/create.html", context)


@require_http_methods(["GET", "POST"])
def update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()

            # 해시태그 업데이트 처리
            new_hashtags = request.POST.get('new_hashtags', '')
            if new_hashtags:
                # 해시태그를 '#'으로 시작하는 부분만 추출하여 리스트로 저장
                hashtags = [tag.strip('#') for tag in new_hashtags.split() if tag.startswith('#')]

                ### 해시태그 검증 로직 추가 ###
                valid_hashtags = []
                for tag in hashtags:
                    if re.search(r'\s', tag):  # 공백이 포함되어 있는지 확인
                        form.add_error(None, f"해시태그 '{tag}'는 공백을 포함할 수 없습니다.")
                    elif re.search(r'[^a-zA-Z0-9가-힣]', tag):  # 특수문자가 포함되어 있는지 확인
                        form.add_error(None, f"해시태그 '{tag}'는 특수문자를 포함할 수 없습니다.")
                    else:
                        valid_hashtags.append(tag)
                
                if form.errors:  # 유효하지 않은 해시태그가 있을 경우, 폼을 다시 렌더링
                    context = {
                        'form': form,
                        'product': product,
                        'existing_hashtags': ' '.join([f'#{hashtag.content}' for hashtag in product.hashtags.all()])
                    }
                    return render(request, 'products/update.html', context)
                
                product.hashtags.clear()  # 기존 해시태그를 모두 지움
                for tag in valid_hashtags:  # 유효한 해시태그만 추가
                    hashtag, created = Hashtag.objects.get_or_create(content=tag)
                    product.hashtags.add(hashtag)

            product.save()
            return redirect('products:detail', pk=pk)
    else:
        form = ProductForm(instance=product)
    context = {
        'form': form,
        'product': product,
        'existing_hashtags': ' '.join([f'#{hashtag.content}' for hashtag in product.hashtags.all()])
    }

    return render(request, 'products/update.html', context)


@login_required
@require_POST
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user == product.author or request.user.is_staff:
        product.delete()
        return redirect('products:products')
    else:
        return redirect('products:detail', pk=pk)


@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        # request.user가 상품을 이미 좋아요 한 상태이면 좋아요한 유저에서 delete
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
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
        ).distinct()
        
        context = {
            'products': products,
            'searched': searched,
        }
        return render(request, 'products/search.html', context)
    else:
        return render(request, 'products/search.html')
