from django.db import models
from django.contrib.auth import get_user_model

# start by creating a class for a resource
class Comment(models.Model):
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner'
    )
    resource = models.ForeignKey('Resource', on_delete=models.CASCADE, related_name='resource')
    # create a string method
    def __str__(self):
        return f"The comment is: {self.comment}. "
