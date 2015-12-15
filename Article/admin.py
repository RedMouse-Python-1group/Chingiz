from django.contrib import admin
from Article.models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
