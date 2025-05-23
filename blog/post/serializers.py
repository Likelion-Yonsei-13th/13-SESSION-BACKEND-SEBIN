from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content',]
        read_only_fields = ['id']

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'created_at', 'updated_at', 'title', 'content']
        read_only_fields = ['id', 'user', 'created_at']


# class PostListSerializer(serializers.ModelSerializer):
#     nickname = serializers.CharField(source='user.nickname', read_only=True)
#     class Meta:
#         model = Post
#         fields = ['title', 'content', 'nickname',]


# class CommentCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ['content', ]        

# class CommentListSerializer(serializers.ModelSerializer):
#     nickname = serializers.CharField(source='user.nickname', read_only=True)
#     class Meta:
#         model = Comment
#         fields = ['id', 'post_id','content', 'nickname',]