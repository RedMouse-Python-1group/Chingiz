from django.shortcuts import render, render_to_response
from Article.models import Article, Comment

# Create your views here.


def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all()})


def article(request, article_id=1):
    return render_to_response('article.html', {'article': Article.objects.get(id=article_id), 'comments': Comment.objects.filter(comments_article_id=article_id)})

