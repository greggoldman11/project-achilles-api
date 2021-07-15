from django.db import models
from django.contrib.auth import get_user_model

# start by creating a class for a resource
class Resource(models.Model):
  # define the different fields:
  # NAME
    name = models.CharField(max_length=100)
    # description
    description = models.CharField(max_length=500)
    # category/tag
    category = models.CharField(max_length=100)
    # url field
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    # create a string method
    def __str__(self):
        return f"The resource named {self.name} is in the category: {self.category}."
