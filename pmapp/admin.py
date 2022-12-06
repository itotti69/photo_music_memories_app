from django.contrib import admin
# 管理サイトの方でポストの内容を参照できるようにする。
from .models import Post, Like, Category, Genre, Tags, Comment

# 管理画面の表示内容を定義するファイル
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'created_at', 'update_at', 'date_at')
    list_display_links = ('title',)
    # created_atの新しい順に並び替えたい
    # １個でもリストとして認識させるために,（カンマ）をつける
    ordering = ('-created_at',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'post_pk')
    list_display_links = ('post',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'target')
    list_display_links = ('text',)