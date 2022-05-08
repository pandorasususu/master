from django.db import models
from django.conf import settings

# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image는 나중에 다시
    # image = models.ImageField(upload_to = user_path)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
    article = models.ForeignKey(Article, on_delete=models.PROTECT, related_name='comments')
    content = models.CharField(max_length=500)
    # image는 나중에 다시
    # image = models.ImageField(upload_to = user_path)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
