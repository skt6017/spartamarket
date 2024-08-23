from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required
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
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():  
            product = form.save(commit=False)
            product.author = request.user
            product.view_count = 1
            product.save()
        return redirect("products:detail", product.pk)
      
    else:
        form = ProductForm()
        
    context = {"form": form}
    return render(request, "products/products_create.html", context)
