from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField('Tag', through='ArticleTag', related_name='articles')

    def __str__(self):
        return "제목: " + self.title + ", 내용: " + self.content + ", 작성일: " + str(self.created_at) + ", 수정일: " + str(self.updated_at)


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "내용: " + self.content + ", 작성일: " + str(self.created_at)


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ArticleTag(models.Model):
    article = models.ForeignKey(Article, related_name='article_tags', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='article_tags', on_delete=models.CASCADE)

