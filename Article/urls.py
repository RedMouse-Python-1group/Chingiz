from django.conf.urls import url

urlpatterns = [
    url(r'^articles/all/$', 'Article.views.articles'),
    url(r'^articles/(?<article_id>)\d+/$', 'Article.views.article'),
]