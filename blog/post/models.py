from django.db import models
from user.models import CustomUser

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser,  on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser,  on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"Comment on {self.post.title} by ID {self.id}"