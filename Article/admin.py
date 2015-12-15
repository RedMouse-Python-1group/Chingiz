from django.contrib import admin
from Article.models import Article, Comment, Image


class ArticleInline(admin.StackedInline):
    model = Image
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date', 'article_user']
    list_filter = ['article_date']
    inlines = [ArticleInline]


class CommentAdmin(admin.ModelAdmin):
    list_filter = ['comments_date']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
