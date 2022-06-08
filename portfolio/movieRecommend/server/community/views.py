from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Count

from rest_framework.response import Response
from rest_framework.decorators import api_view

from users import serializers

# model, serializers
from .models import Article, Comment
from .serializers.article import ArticleListSerializer, ArticleSerializer
from .serializers.comment import CommentSerializer

# Create your views here.

# 0608 당장은 status를 가지고 할 수 있는 일이 적은 것 같아서 제외시킴

@api_view(['GET', 'POST'])
def read_or_create_articles(request):
    def read_article_list():
        articles = Article.objects.annotate(
            comment_count=Count('comments',distinct=True),
            like_count=Count('like_users',distinct=True),
            dislike_count=Count('dislike_users',distinct=True),
        ).order_by('-updated_at')

        serializer = ArticleListSerializer(articles)
        return Response(serializer.data)

    def create_article():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)

    if request.method == 'GET':
        return read_article_list()
    elif request.method == 'POST':
        return create_article()

@api_view(['GET','PUT', 'DELETE'])
def detail_update_or_delete_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        now_like = True
    else:
        now_like = False

    def detail_article():
        serializer = ArticleSerializer(article)
        return Response(serializer.data, now_like)
    def update_article():
        if request.user == article.user:
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, now_like)
    def delete_article():
        if request.user == article.user:
            article.delete()
            context = {
                'delete_msg': '성공적으로 게시글을 삭제했습니다.'
            }
            return Response(context)

    if request.method == 'GET':
        return detail_article()
    elif request.method == 'PUT':
        return update_article()
    elif request.method == 'DELETE':
        return delete_article()

@api_view(['POST'])
def like_article(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)

    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
        now_like = False
    else:
        article.like_users.add(user)
        now_like = True

    serializer = ArticleSerializer(article)
    return Response(serializer.data, now_like)

@api_view(['POST'])
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article,user=user)
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

        # 새로 만들어진 comment 하나만 serialize해서 return하는 경우
        # return Response(serializer.data)
        # 나중에 이 방법으로도 시도해 볼 것
        # 아래의 댓글 수정과 같은 경우는, 수정될 댓글의 위치 때문에 모든 댓글을 serialize할 수 밖에 없지만, 새로운 댓글을 
        # 만들 때는 하나의 댓글만 보내줘도 되지 않을까?



@api_view(['PUT', 'DELETE'])
def update_or_delete_comment(request, article_pk, comment_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    # comment의 like_users 중 로그인한 유저가 있다면 now_like=True, 아니면 False
    if comment.like_users.filter(pk=user.pk).exists():
        now_like = True
    else:
        now_like = False

    def update_comment():
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, now_like)

    def delete_comment():
        comment.delete()
        comments= article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        context = {
            'delete_msg': '성공적으로 댓글을 삭제했습니다.'
        }
        return Response(serializer.data, context)

    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()

@api_view(['POST'])
def like_comment(request, article_pk, comment_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if comment.like_users.filter(pk=user.pk).exists():
        comment.like_users.remove(user)
        now_like = False
    else:
        comment.like_users.add(user)
        now_like = True
    
    comments = article.comments.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, now_like)

