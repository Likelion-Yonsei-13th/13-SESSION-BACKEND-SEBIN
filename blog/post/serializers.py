from rest_framework import serializers
from .models import Post, Comment

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content',]

class PostListSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Post
        fields = ['title', 'content', 'nickname',]


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', ]        

class CommentListSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'post_id','content', 'nickname',]