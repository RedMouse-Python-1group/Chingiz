from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from tinymce import models as tinymce_models


# Create your models here.


class Article(models.Model):
    class Meta:
        db_table = 'article'

    article_title = tinymce_models.HTMLField(max_length=200)
    article_text = tinymce_models.HTMLField()
    article_date = models.DateField()
    article_user = models.ForeignKey(User)
    article_likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.article_title


class Comment(models.Model):
    class Meta:
        db_table = 'comments'

    comments_text = tinymce_models.HTMLField()
    comments_article = models.ForeignKey(Article)


class Image(models.Model):
    class Meta:
        db_table = 'images'

    image = models.ImageField(upload_to="uploads", help_text="Do not add too large pics, please")
    images_article = models.ForeignKey(Article)
