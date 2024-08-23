from django.urls import path, include
from . import views
from django.urls import path

app_name="products"
urlpatterns = [
    path('', views.products, name="products"),
    path('<int:pk>/', views.detail, name="detail"),
    path('create/', views.product_create, name='product_create'),
    path('update/<int:pk>/', views.product_update, name='product_update'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('<int:pk>/like/', views.like, name='like'),

    ]
