from django.contrib import admin
from Article.models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date']
    list_filter = ['article_date']


class CommentAdmin(admin.ModelAdmin):
    list_filter = ['comments_date']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
