from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    # symmetrical을 False로 설정함으로써 한 쪽이 팔로우 하더라도 상호 팔로우 되지 않음
    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    rated_movies = models.IntegerField(null=True)

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
    # TMDB DB에 저장된 영화의 ID를 저장
    movie_id = models.IntegerField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_ratings')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_ratings')

    # 별점은 0.5점 단위로 들어옴
    star_rating = models.FloatField()
    # 유저가 추가로 의견을 적지 않는 이상, 별점을 기준으로 0점~1점 '비추천', 1.5점~3.5점 '무난', 4점~5점 '추천' 이라는 단어가 default로 들어옴
    comment_rating = models.CharField(max_length=500)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# chrome-extension 만들기 전에, 기능을 구현해보고 싶어서 추가함
# community의 article들 중, 저장해서 계속 보고 싶은 글들 중에 saveable 옵션이 true인 경우, 저장할 수 있음
# 추후에는 여기에 드래그해서 하이라이트 하는 기능, 메모를 추가하는 기능을 구현하고 싶음
# 하지만 기본 기능 다 구현하고 생각하는 걸로, 일단 주석처리
# class SavedArticle(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='saved_articles')
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)