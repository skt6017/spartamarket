from django.urls import path
from. import views

app_name="products"
urlpatterns = [
    path('', views.products, name="products"),
    path('<int:pk>/', views.detail, name="detail"),
    path('create/', views.create, name='create'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('<int:pk>/like/', views.like, name='like'),
    path('<int:hashtag_pk>/hashtag/', views.hashtag, name='hashtag'), # hashtag detail page

    ]
