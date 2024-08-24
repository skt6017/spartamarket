from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "accounts"
urlpatterns = [
    
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("delete/",views.delete, name="delete"),
    path("update/",views.update, name="update"),
    path("password/",views.change_password, name="change_password"),
    path("profile_view/",views.profile_view, name="profile_view"),
    path('profile/<str:username>/', views.profile_view, name='profile'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
