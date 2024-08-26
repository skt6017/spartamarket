from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


@require_http_methods(["GET","POST"])
def login(request):
    if request.method =="POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get("next") or "index"
        return redirect(next_url)
    else:
        form = AuthenticationForm()
        
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('index')

@require_http_methods(["GET","POST"])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    context={'form': form}
    return render(request, 'accounts/signup.html', context)

@login_required
@require_http_methods(["GET","POST"])   
def update(request):
    if request.method =="POST":
        form =CustomUserChangeForm (request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form" :form}
    return render(request, "accounts/update.html", context)

@require_http_methods(["GET","POST"])
def change_password(request):
    if request.method=="POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
        return redirect("index")
    else: 
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, "accounts/change_password.html", context)


@login_required
@require_POST 
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("index")