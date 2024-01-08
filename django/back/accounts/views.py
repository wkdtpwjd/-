from django.shortcuts import render
from .serializers import ProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.
@api_view(['GET','PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
def profile(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    if request.method == 'GET':
        serializer = ProfileSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = ProfileSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def followings(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    if request.method == 'GET':
        followings = user.followings.all()
        serializer = ProfileSerializer(instance=followings, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if request.user in user.followings.all():
            user.followings.remove(request.user)
            return Response('팔로잉에 삭제되었습니다.',status=status.HTTP_202_ACCEPTED)
        else:
            user.followings.add(request.user)
            return Response('팔로잉에 추가되었습니다.',status=status.HTTP_202_ACCEPTED)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def followers(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    if request.method == 'GET':
        followings = user.followers.all()
        serializer = ProfileSerializer(instance=followings, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if request.user in user.followers.all():
            user.followers.remove(request.user)
            return Response('팔로잉에 삭제되었습니다.',status=status.HTTP_202_ACCEPTED)
        else:
            user.followers.add(request.user)
            return Response('팔로잉에 추가되었습니다.',status=status.HTTP_202_ACCEPTED)