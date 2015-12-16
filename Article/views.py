from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, render_to_response, redirect
from Article.models import Article, Comment, Image

# Create your views here.


def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all()})


def article(request, article_id=1):
    return render_to_response('article.html', {'article': Article.objects.get(id=article_id), 'comments': Comment.objects.filter(comments_article_id=article_id)})


def addlike(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        article.article_likes += 1
        article.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

