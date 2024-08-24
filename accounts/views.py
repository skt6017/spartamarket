# accounts/views.py

from profile import Profile
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    PasswordChangeForm
)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST,require_http_methods
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import update_session_auth_hash

from .forms import CustomUserChangeForm
from .models import Profile
from .forms import CustomUserCreateForm



# Create your views here.
@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get("next") or "index"
            return redirect(next_url)  # 여기서 문자열이 아닌 변수로 처리
    else:
        form = AuthenticationForm()

    context = {"form": form}
    return render(request, "accounts/login.html", context)

@require_POST
def logout(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect("index")

@require_http_methods(["GET","POST"])
def signup(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():    
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("index")
        else:
            print(form.errors)

    else:
        form = CustomUserCreateForm()
    context = {"form" :form}
    return render(request, "accounts/signup.html", context)

@require_POST 
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect("index")
    
    
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

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # 세션을 유지하도록 해줍니다.
            return redirect("index")
    else:
        form = PasswordChangeForm(request.user)
    context = {"form": form}
    return render(request, "accounts/change_password.html", context)


# 프로필 구현
def profile_view(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    context = {
        'profile': profile
    }
    return render(request, 'accounts/profile.html', context)



# @login_required
# def profile_edit(request):
#     if request.method == 'POST':
#         user_form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
#         if user_form.is_valid():
#             user_form.save()  # User 모델 업데이트
#             profile, created = Profile.objects.get_or_create(user=request.user)
#             profile.image = user_form.cleaned_data.get('profile_image')
#             # profile.work_start = user_form.cleaned_data.get('work_start')
#             # profile.work_end = user_form.cleaned_data.get('work_end')
#             # profile.bio = user_form.cleaned_data.get('bio')
#             # profile.birthday = user_form.cleaned_data.get('birthday')
#             profile.save()  # Profile 모델 업데이트
#             return redirect('profile')  # 프로필 페이지로 리디렉션
#     else:
#         user_form = CustomUserChangeForm(instance=request.user)
#     return render(request, 'profile_edit.html', {'form': user_form})