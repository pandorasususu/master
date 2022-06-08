from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Article, Comment
from ..models import Rating
User = get_user_model()

class UserProfileSerilizer(serializers.ModelSerializer):

    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('pk', 'title',)
    like_articles = ArticleSerializer(many=True)
    articles = ArticleSerializer(many=True)

    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('pk', 'content',)
    like_comments = CommentSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = User
        fields = ('pk','username', 'email', 'followings', 'followers', 'like_articles','articles','like_comments','comments',)