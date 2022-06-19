from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Article, Comment

# 프로필
class ProfileSerializer(serializers.ModelSerializer):

    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('pk', 'title', 'content')

    like_articles = ArticleSerializer(many=True)
    articles = ArticleSerializer(many=True)

    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('pk', 'content', 'article')
    like_comments = CommentSerializer(many=True)
    comments = CommentSerializer(many=True)
    
    #0523lbh 'followings', 'followers', 'like_comments' 불러오기
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'followings', 'followers' ,'like_articles', 'articles','like_comments', 'comments',)
