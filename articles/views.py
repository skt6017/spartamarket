from django.shortcuts import get_object_or_404, render,redirect
from .models import  Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    return render(request, "articles/index.html")

def articles(request):
    articles = Article.objects.all().order_by("id")
    context = {
        "articles":articles,
    }
    return render(request, "articles/articles.html",context)


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)

    
    context ={
        "article":article}
    return render(request, "articles/article_detail.html",context)

    
@login_required
def create(request):    
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            # 이미지 파일이 있는지 확인한 후 경로를 출력
            if article.image and hasattr(article.image, 'path'):
                print(f"File saved to: {article.image.path}")  # 저장된 이미지 경로 출력
            else:
                print("No image file associated with this article.")
            return redirect("articles:article_detail", article.id)
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = ArticleForm()
        
    context = {"form": form}
    return render(request, "articles/create.html", context)

def update(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("articles:article_detail", article.id)
    else:
        form = ArticleForm(instance=article)
    context = {
        "form": form,
        "article": article,
    }
    return render(request, "articles/update.html", context)
    
    
@require_POST 
def delete(request, id):
    if request.user.is_authenticated:
            article = get_object_or_404(Article, id=id)
            article.delete()
            return redirect("articles:articles")
    return redirect("articles:article_detail",id)




def data_throw(request):
    return render(request, "articles/data_throw.html")

def data_catch(request):
    message = request.GET.get("message")
    context = {
        "message" : message 
            }
    return render(request, "articles/data_catch.html",context)
