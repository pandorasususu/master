from rest_framework import serializers
from .models import Movie, Genre, Rating
from django.contrib.auth import get_user_model

User = get_user_model()

# movie 목록
class MovieListSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name')
    
    # 장르 id 참조
    genre_ids = GenreSerializer(many=True, read_only=True) 

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre_ids', 'release_date', 'poster_path')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('user', 'movie', 'score', 'genre_ids')
        read_only_fields = ('user', 'movie',)

