from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# model, serializers
from .serializers import UserProfileSerilizer

# Create your views here.

User = get_user_model()

# 유저 프로필
@api_view(['GET'])
def user_profile(request, username):
    viewed_user = get_object_or_404(User, username=username)
    serializer = UserProfileSerilizer(viewed_user)
    return Response(serializer.data)

# 유저 팔로우/팔로우 취소 기능
# 과제로 제출한 프로젝트에서는 팔로우 할 때 마다 UserProfileSerilizer를 통해 모든 정보를 다시 보내줬음
# 팔로우 여부에 대한 정보만 전달하는 것이 적절하다고 판단해서 수정
@api_view(['POST'])
def user_follow(request, username):
    target = get_object_or_404(User, username=username)
    current_user = request.user
    
    if target != current_user:
        if target.followers.filter(pk=current_user.pk).exists():
            target.followers.remove(current_user)
            now_following = False
        else:
            target.followers.add(current_user)
            now_following = True
    return Response(now_following)