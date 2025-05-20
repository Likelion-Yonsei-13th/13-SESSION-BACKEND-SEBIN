from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Post, Comment
from .serializers import PostCreateSerializer, PostListSerializer, CommentCreateSerializer, CommentListSerializer

"""------------POST CRUD---------------"""

#포스트 전체 조회
@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostListSerializer(posts,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 포스트 생성
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_post(request):
    serializer = PostCreateSerializer(data=request.data)
    
    # is_valid : serializer에서 필요로하는 field값이 잘 들어왔는지...
    if serializer.is_valid():
        # db에 저장(python 객체를)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#포스트 수정
@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({'error' : 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if post.user != request.user:
        return Response({'error':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    serializer = PostCreateSerializer(post, data=request.data)

    if serializer.is_valid():
        serializer.save(user=post.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#포스트 삭제
@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({'error' : 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if post.user != request.user:
        return Response({'error':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    post.delete()
    return Response({'message': '삭제 완료'}, status=status.HTTP_204_NO_CONTENT)



"""------------Comment---------------"""
#포스트 별 댓글 조회
@api_view(['GET'])
def comment_list(request, post_id):
    comments = Comment.objects.filter(post_id=post_id)
    serializer = CommentListSerializer(comments,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#댓글 생성
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_comment(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CommentCreateSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save(user=request.user, post=post)  
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#댓글 수정
@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_comment(request, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        return Response({'error' : 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if comment.user != request.user:
        return Response({'error':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    serializer = CommentCreateSerializer(comment, data=request.data)

    if serializer.is_valid():
        serializer.save(user=comment.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#댓글 삭제
@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_comment(request, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        return Response({'error' : 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if comment.user != request.user:
        return Response({'error':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    comment.delete()
    return Response({'message': '삭제 완료'}, status=status.HTTP_204_NO_CONTENT)