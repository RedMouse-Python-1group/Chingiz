from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, render_to_response, redirect
from django.template.context_processors import csrf

from Article.forms import CommentForm
from Article.models import Article, Comment, Image

# Create your views here.


def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all()})


def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comment.objects.filter(comments_article_id=article_id)
    args["form"] = comment_form
    return render_to_response('article.html', args)


def addlike(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        article.article_likes += 1
        article.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def addcomment(request, article_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            foo = "/articles/%s/" % article_id
    return redirect(foo)
