from django.db import models
from django.conf import settings


class Hashtag(models.Model):
    content = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.content
    
    
class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="product_img/", blank=True)
    view_count = models.IntegerField(default=0)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products"
    )

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_products"
    )
    hashtags = models.ManyToManyField(Hashtag, blank=True) # hashtags to product 추가
    
    def __str__(self):
        return self.title  
    
