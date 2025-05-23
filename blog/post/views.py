from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
class PostView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many =True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PostDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise Response({"error":"게시글을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
    def get(self, post_id):
        post = self.get_object(post_id)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, post_id):
        try:
            post = self.get_object(post_id)
        except Post.DoesNotExist:
            return Response({"error":"게시글을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        if post.user != request.user:
            return Response({"error":"본인 게시글만 수정할 수 있습니다."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = PostDetailSerializer(post, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, post_id):
        try:
            post = self.get_object(post_id)
        except Post.DoesNotExist:
            return Response({"error":"게시글을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        if post.user != request.user:
            return Response({"error":"본인 게시글만 삭제할 수 있습니다."}, status=status.HTTP_403_FORBIDDEN)
        
        post.delete()
        return Response({"message": "게시글이 성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
"""------------POST CRUD---------------"""


# """------------Comment---------------"""
# #포스트 별 댓글 조회
# @api_view(['GET'])
# def comment_list(request, post_id):
#     comments = Comment.objects.filter(post_id=post_id)
#     serializer = CommentListSerializer(comments,many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

# #댓글 생성
# @api_view(['POST'])
# @permission_classes([permissions.IsAuthenticated])
# def create_comment(request, post_id):
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

#     serializer = CommentCreateSerializer(data=request.data)
    
#     if serializer.is_valid():
#         serializer.save(user=request.user, post=post)  
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #댓글 수정
# @api_view(['PUT'])
# @permission_classes([permissions.IsAuthenticated])
# def update_comment(request, comment_id):
#     try:
#         comment = Comment.objects.get(id=comment_id)
#     except Comment.DoesNotExist:
#         return Response({'error' : 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
    
#     if comment.user != request.user:
#         return Response({'error':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
#     serializer = CommentCreateSerializer(comment, data=request.data)

#     if serializer.is_valid():
#         serializer.save(user=comment.user)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #댓글 삭제
# @api_view(['DELETE'])
# @permission_classes([permissions.IsAuthenticated])
# def delete_comment(request, comment_id):
#     try:
#         comment = Comment.objects.get(id=comment_id)
#     except Comment.DoesNotExist:
#         return Response({'error' : 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
    
#     if comment.user != request.user:
#         return Response({'error':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
#     comment.delete()
#     return Response({'message': '삭제 완료'}, status=status.HTTP_204_NO_CONTENT)