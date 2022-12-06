from django.db import models
from pmapp.models import Post

class Comment(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)