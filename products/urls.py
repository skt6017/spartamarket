from django.urls import path
from. import views

app_name="products"
urlpatterns = [
    path('create/', views.product_create, name='product_create'),
    ]
