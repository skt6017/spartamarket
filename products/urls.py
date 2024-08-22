from django.urls import path
from. import views

app_name="products"
urlpatterns = [
    path('create/', views.product_create, name='product_create'),
    path('update/<int:pk>/', views.product_update, name='product_update'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('', views.product_list, name='product_list'),
    ]
