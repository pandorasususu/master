from django.db import models
from django.conf import settings

# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_articles')
    save_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='save_articles')
    # 특정 영화 관련 tag를 저장하는 column을 만들고 싶음. 어떻게 구현할 수 있을 지 모르니 일단 만들어만 두고 주석처리
    # 영화 관련된 정보들이 db에 저장되어 있으면 manytomanyfield 통해 쉽게 구현할 수 있겠지만, 영화 관련 정보는 전부 TMDB API를 활용하려고 함
    # 게시물 작성 페이지에서 관련 영화를 입력할 수 있는 input을 만들고, 해당 input에 영화의 제목을 입력할 경우 TMDB에 있는 영화 제목을 알려주고, 
    # 자동완성 기능을 통해 해당 제목을 받아오면 될 거 같은데, 이것을 어떻게 구현할 수 있을까? 
    # movies = models.CharField(max_length=200, null=True)

    # 게시글에 이미지 추가할 수 있는 것도 나중에 구현

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 다른 유저가 해당 게시글을 저장할 수 있는지 여부
    saveable = models.BooleanField(default=True)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_comments')

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
