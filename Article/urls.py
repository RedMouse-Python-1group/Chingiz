from django.conf.urls import url

urlpatterns = [
    url(r'^articles/(?P<article_id>\d+)/$', 'Article.views.article'),
    url(r'^$', 'Article.views.articles'),
]