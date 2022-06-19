from audioop import avg
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Movie, Rating, Genre
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieListSerializer, RatingSerializer
import random
import time
from django.db.models import Avg
from operator import itemgetter
# Create your views here.

User = get_user_model()

@api_view(['GET'])
def movie_list_random_get(request):
    movies = get_list_or_404(Movie)
    movies_random = random.sample(movies, 10)
    serializer = MovieListSerializer(movies_random, many=True)
    return Response(serializer.data)

# movie 목록
@api_view(['GET'])
def movie_list_get(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# movie 단일, 'id','total_rating', 'like_users',만
@api_view(['GET'])
def movie_detail(request, movie_id):
    user = request.user
    if Rating.objects.filter(user_id=user.id, movie_id=movie_id).exists():
        user_rate = Rating.objects.get(user_id=user.id, movie_id=movie_id).score
        already_rated = True
    else:
        user_rate = 0
        already_rated = False
    rating_avg = Rating.objects.filter(movie_id=movie_id).aggregate(Avg('score'))
    rated_user = Rating.objects.filter(movie_id=movie_id).count()
    context = {
        'rating_avg': rating_avg,
        'rated_user': rated_user,
        'user_rate': user_rate,
        'already_rated': already_rated,
    }
    return Response(context)



@api_view(['POST'])
def movie_save(request, movie_id):
    request_id = request.data['movie']['id']
    if Movie.objects.filter(id=request_id).exists():
        return Response(status=status.HTTP_200_OK)
    else:
        serializer = MovieListSerializer(data=request.data['movie'])
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST', 'PUT'])
def movie_rating(request, movie_id, username):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = get_object_or_404(User, username=username)
    if Rating.objects.filter(user_id=user.id, movie_id=movie_id).exists():
        Rating.objects.filter(user_id=user.id, movie_id=movie_id).delete()
    serializer = RatingSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user, movie=movie)
    return Response(serializer.data)

    


@api_view(['GET'])
def movie_recommend(request, username):
    user = get_object_or_404(User, username=username)
    user_ratings = user.ratings.all()

    genre = get_list_or_404(Genre)
    genre_list = {}
    for g in genre:
        genre_list[g.id] = {'id':g.id ,'name': g.name, 'rating_count': 0, 'rating_total': 0, 'rating_avg': 0}    
    for e in user_ratings:
        genre_ids = e.genre_ids.split(',')
        for g in genre_ids:
            g = int(g)
            genre_list.get(g)['rating_count'] += 1
            genre_list.get(g)['rating_total'] += e.score
            genre_list.get(g)['rating_avg'] = round(genre_list.get(g)['rating_total'] / genre_list.get(g)['rating_count'], 1)

    genre_list_all = genre_list.values()
    genre_list_rating_count = sorted(genre_list_all, key=itemgetter('rating_count'), reverse=True)[0]
    genre_list_rating_avg = sorted(genre_list_all, key=itemgetter('rating_avg'), reverse=True)[0]
    context = {
        'genre_list_all': genre_list_all,
        'genre_list_rating_count': genre_list_rating_count,
        'genre_list_rating_avg': genre_list_rating_avg,
    }
    return Response(context)


# 평점 높은 순
@api_view(['GET'])
def movie_toprated(request):
    if request.method == 'GET':
        movies = Movie.objects.order_by('-vote_average')[:30]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

# 인기순
@api_view(['GET'])
def movie_popular(request):
    if request.method == 'GET':
        movies = Movie.objects.order_by('-popularity')[:30]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

# 최근 개봉순
@api_view(['GET'])
def movie_recent(request):
    if request.method == 'GET':
        movies = Movie.objects.order_by('-release_date')[:30]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)