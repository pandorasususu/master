from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Count, Avg

from rest_framework.response import Response
from rest_framework.decorators import api_view

# model, serializers
from .serializers.user import UserProfileSerilizer
from .serializers.rating import RatingSerializer, RatingListSerializer
from .models import Rating

# Create your views here.

User = get_user_model()

# 유저 프로필
@api_view(['GET', 'POST'])
def user_profile_or_follow(request, username):
    viewed_user = get_object_or_404(User, username=username)
    current_user = request.user

    def user_profile():
        if viewed_user != current_user:
            if viewed_user.followers.filter(pk=current_user.pk).exists():
                now_following = True
            else:
                now_following = False
            serializer = UserProfileSerilizer(viewed_user)
            context = {
                'data': serializer.data,
                'now_following': now_following,
                # followings/followers 는 array 형태의 데이터, 이의 length를 통해 아래의 결과를 똑같이 얻을 수 있음
                # 'followings_count': User.objects.filter(id=viewed_user.id).aggregate(Count('followings'))['followings__count'],
                # 'followers_count': User.objects.filter(id=viewed_user.id).aggregate(Count('followers'))['followers__count']
            }
            return Response(context)
        
        else:
            serializer = UserProfileSerilizer(viewed_user)
            context = {
                'data': serializer.data,
                # 'followings_count': User.objects.filter(id=viewed_user.id).aggregate(Count('followings'))['followings__count'],
                # 'followers_count': User.objects.filter(id=viewed_user.id).aggregate(Count('followers'))['followers__count']
            }
            return Response(context)

    
    def user_follow():
    
        if viewed_user != current_user:
            if viewed_user.followers.filter(pk=current_user.pk).exists():
                viewed_user.followers.remove(current_user)
                now_following = False
            else:
                viewed_user.followers.add(current_user)
                now_following = True
            serializer = UserProfileSerilizer(viewed_user)
        context = {
            'data': serializer.data,
            'now_following': now_following,
            # 'followings_count': User.objects.filter(id=viewed_user.id).aggregate(Count('followings'))['followings__count'],
            # 'followers_count': User.objects.filter(id=viewed_user.id).aggregate(Count('followers'))['followers__count']
        }
        return Response(context)   

    if request.method == 'GET':
        return user_profile()
    elif request.method == 'POST':
        return user_follow()

        
# 유저 팔로우/팔로우 취소 기능
# 과제로 제출한 프로젝트에서는 팔로우 할 때 마다 UserProfileSerilizer를 통해 모든 정보를 다시 보내줬음
# 팔로우 여부에 대한 정보만 전달하는 것이 적절하다고 판단해서 수정
# @api_view(['POST'])
# def user_follow(request, username):
#     target = get_object_or_404(User, username=username)
#     current_user = request.user
    
#     if target != current_user:
#         if target.followers.filter(pk=current_user.pk).exists():
#             target.followers.remove(current_user)
#             now_following = False
#         else:
#             target.followers.add(current_user)
#             now_following = True
#         serializer = UserProfileSerilizer(target)
#     context = {
#         'now_following': now_following,
#         'followings_count': User.objects.get(id=target.id).Count('followings'),
#         'followers_count': User.objects.get(id=target.id).Count('followers')
#     }
#     return Response(serializer.data, context)


@api_view(['GET','POST'])
def read_or_create_rating(request, movie_id):
    user = request.user

    def read_ratings():
        rating_list = Rating.objects.annotate(
            like_count=Count('like_users', distinct=True),
            dislike_count=Count('dislike_users', distinct=True),
            avg_star_rating=Avg('star_rating', distinct=True)
        ).get(movie_id=movie_id)
        serializer_list = RatingListSerializer(rating_list, many=True)
        if Rating.objects.filter(user=user, movie_id=movie_id).exists():
            user_rating = get_object_or_404(Rating, user=user, movie_id=movie_id)
            serializer_single = RatingSerializer(user_rating)
            rating_exists = True

            context = {
                'rating_list_data': serializer_list.data,
                'rating_mine_data': serializer_single.data,
                'rating_exists': rating_exists,
            }
            return Response(context)
        else:
            rating_exists = False
            context = {
                'rating_list_data': serializer_list.data,
                'rating_exists': rating_exists,
            }
            return Response(context)

    def create_rating():
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, movie_id=movie_id)
            return Response(serializer.data)
    
    if request.method == 'GET':
        return read_ratings()
    elif request.method == 'POST':
        return create_rating()

@api_view(['PUT', 'DELETE'])
def update_or_delete_rating(request, movie_id, rating_pk):
    user = request.user
    rating = get_object_or_404(Rating, pk=rating_pk)

    def update_rating():
        serializer_single = RatingSerializer(rating, data=request.data)
        if serializer_single.is_valid(raise_exception=True):
            serializer_single.save()

            rating_list = Rating.objects.annotate(
                like_count=Count('like_users', distinct=True),
                dislike_count=Count('dislike_users', distinct=True),
                avg_star_rating=Avg('star_rating', distinct=True)
            ).get(movie_id=movie_id)
            serializer_list = RatingListSerializer(rating_list, many=True)

            rating = get_object_or_404(Rating, pk=rating_pk)
            serializer_single = RatingSerializer(rating)

            context = {
                'rating_list_data': serializer_list.data,
                'rating_mine_data': serializer_single.data,
            }
            return Response(context)

    def delete_rating():
        rating.delete()
        rating_list = Rating.objects.annotate(
            like_count=Count('like_users', distinct=True),
            dislike_count=Count('dislike_users', distinct=True),
            avg_star_rating=Avg('star_rating', distinct=True)
        ).get(movie_id=movie_id)
        serializer_list = RatingListSerializer(rating_list, many=True)
        return Response(serializer_list.data)

    if request.method == 'PUT':
        return update_rating()
    elif request.method == 'DELETE':
        return delete_rating()
        
@api_view(['POST'])
def like_rating(request, movie_id, rating_pk):
    rating = get_object_or_404(Rating, pk=rating_pk)
    user = request.user

    if rating.like_users.filter(user=user).exists():
        rating.like_users.remove(user)
    else:
        rating.like_users.add(user)
    
    rating_list = Rating.objects.annotate(
        like_count=Count('like_users', distinct=True),
        dislike_count=Count('dislike_users', distinct=True),
        avg_star_rating=Avg('star_rating', distinct=True)
    ).get(movie_id=movie_id)
    serializer_list = RatingListSerializer(rating_list, many=True)

    rating = get_object_or_404(Rating, pk=rating_pk)
    serializer_single = RatingSerializer(rating)
    context = { 
        'rating_list_data': serializer_list.data,
        'rating_mine_data': serializer_single.data,
    }
    return Response(context)

