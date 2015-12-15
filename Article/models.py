from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Article(models.Model):
    class Meta:
        db_table = 'article'

    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateField()
    article_user = models.ForeignKey(User)
    article_likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.article_title


class Comment(models.Model):
    class Meta:
        db_table = 'comments'

    comments_text = models.TextField()
    comments_date = models.DateField()
    comments_article = models.ForeignKey(Article)


class Image(models.Model):
    class Meta:
        db_table = 'images'

    image = models.ImageField(upload_to="images")
    images_article = models.ForeignKey(Article)
