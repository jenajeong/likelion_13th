from django.contrib import admin

from .models import Article, Comment, Tag, ArticleTag

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    list_per_page = 10


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'content', 'created_at', 'updated_at')
    search_fields = ('content',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    list_per_page = 10


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page = 10


@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('article', 'tag')
    search_fields = ('article__title', 'tag__name')
    list_filter = ('article', 'tag')
    ordering = ('article', 'tag')
    list_per_page = 10
