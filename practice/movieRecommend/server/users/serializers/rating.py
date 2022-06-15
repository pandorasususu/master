from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Rating
User = get_user_model()


class RatingListSerializer(serializers.ModelSerializer):

    like_count = serializers.IntegerField()
    dislikelike_count = serializers.IntegerField()
    avg_star_rating = serializers.FloatField()
    class Meta:
        model = Rating
        fieidls = ('pk', 'user','like_users', 'dislike_users', 'star_rating', 'comment_rating', 'updated_at', 'like_count', 'dislike_count', 'avg_star_rating',)
        read_only_fields = ('user', 'movie_id', )

class RatingSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField()
    dislikelike_count = serializers.IntegerField()

    class Meta:
        model = Rating
        fieidls = ('pk', 'user', 'movie_id', 'like_users', 'dislike_users', 'star_rating', 'comment_rating', 'created_at', 'updated_at', 'like_count', 'dislike_count')
        read_only_fields = ('user', 'movie_id', )
