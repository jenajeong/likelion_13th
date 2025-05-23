from django.db import models
import os
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/', null=True) # 미디어 파일 올리는 방법 (블로그 안에 블로그 파일이 생겨서)

    def __str__(self):
        return self.title

