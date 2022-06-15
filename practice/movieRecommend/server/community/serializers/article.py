from pyexpat import model
from xml.etree.ElementTree import Comment
from rest_framework import serializers
from ..models import Article
from .comment import CommentSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class ArticleSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    dislike_users = UserSerializer(read_only=True, many=True)
    save_users = UserSerializer(read_only=True, many=True)
    comments = CommentSerializer(many=True, read_only=True)


    class Meta:
        model = Article
        fields = ('pk','user','title','content','created_at','updated_at',
        'like_users','dislike_users','save_users', 'saveable', 'comments')

class ArticleListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    like_count = serializers.IntegerField()
    dislike_count = serializers.IntegerField()
    comment_count = serializers.IntegerField() 

    class Meta:
        model = Article
        fields = ('pk','user', 'title', 'updated_at', 'like_count', 'dislike_count', 'comment_count')