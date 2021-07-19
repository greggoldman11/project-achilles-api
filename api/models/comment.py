from django.db import models
from .resource import Resource
from django.contrib.auth import get_user_model

class Comment(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments'
    )
    class Meta:
        ordering = ['created_at',]

    def __str__(self):
        return f'Comment by {self.name} on {self.resource}!'
