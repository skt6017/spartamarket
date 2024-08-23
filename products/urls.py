from django.urls import path, include
from . import views
app_name="products"
urlpatterns = [
    path('', views.products, name="products"),
    path('<int:pk>/', views.detail, name="detail"),
    path('create/', views.product_create, name='product_create'),
    ]
