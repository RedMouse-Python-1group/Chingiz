from django.conf.urls import url

urlpatterns = [
    url(r'^articles/(?P<article_id>\d+)/$', 'Article.views.article'),
    url(r'^articles/addlike/(?P<article_id>\d+)/$', 'Article.views.addlike'),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'Article.views.addcomment'),
    url(r'^$', 'Article.views.articles'),
]