from rest_framework import serializers
from ..models import Comment
from django.contrib.auth import get_user_model


User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    dislike_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Comment
        fields = ('pk', 'user','content', 'updated_at', 'like_users',
        'dislike_users', 'article',)
        read_only_fields = ('article',)