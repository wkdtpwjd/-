from django.shortcuts import render
from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleListSerializer, CommentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# Create your views here.

@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['GET','POST'])
def articles(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(instance=articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['GET','PUT','DELETE'])
def article_detail(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(instance=article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response('삭제되었습니다.', status=status.HTTP_204_NO_CONTENT)
    

@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['GET', 'POST'])
def comments(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        comments = Comment.objects.filter(article=article)
        serializer = CommentSerializer(instance=comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, article=article)
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request,article_pk,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(instance=comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'delete':
        comment.delete()
        return Response('삭제되었습니다.', status=status.HTTP_204_NO_CONTENT)