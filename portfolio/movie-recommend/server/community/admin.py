from django.contrib import admin
from .models import Article, Comment
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    fields = []

class CommentAdmin(admin.ModelAdmin):
    fields = []

admin.site.register(Article, ArticleAdmin) 
admin.site.register(Comment, CommentAdmin)
