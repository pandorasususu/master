from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProfileSerializer

# Create your views here.
User = get_user_model()

# 프로필
@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    # context = {
    #     'followers': user.followers.count(),
    #     'followings': user.followings.count(),
    # }
    # return Response(serializer.data, context)
    return Response(serializer.data)

# # 회원 탈퇴
@api_view(['DELETE'])
def delete(request, username):
    person = get_object_or_404(User, username=username)
    person.delete()
    context = {
        'delete_message': '성공적으로 탈퇴하셨습니다.'
    }
    return Response(context)

# 팔로우
@api_view(['POST'])
def follow(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    user = request.user

    if person != user :
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
            follow = True
        else:
            person.followers.add(user)
            follow = False
        
        serializer = ProfileSerializer(person)

    return Response(serializer.data)
