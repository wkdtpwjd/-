from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404,get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Music,Comment
from .serializers import MusicSerializer,CommentSerializer



@api_view(['GET','POST'])
def music_list(request):
    if request.method == 'GET':
        musics = get_list_or_404(Music)
        serializer = MusicSerializer(musics,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # 새로운 music 저장하기
        serializer = MusicSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    
# 잘못된데이터가 들어왔으면 에러출력 raise_exception=True


@api_view(['GET','PUT','DELETE'])
def music_detail(request,music_pk):
    music = get_object_or_404(Music,pk=music_pk)
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = MusicSerializer(instance=music,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


    elif request.method == 'DELETE':
        data = {
            'delete':f'{music.pk}번 삭제되었습니다'
        }
        music.delete()
        return Response(data,status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def comment_create(request,music_pk):
    music = get_object_or_404(Music,pk=music_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(music=music)
        return Response(serializer.data)




    
@api_view(['GET','PUT','DELETE'])
def comment_detail(request,comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(instance=comment,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        data = {
            'delete':f'{comment.pk}번 댓글 삭제'
        }
        comment.delete()
        return Response(data,status=status.HTTP_204_NO_CONTENT)





@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments,many= True)
        return Response(serializer.data)