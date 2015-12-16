from django.forms import ModelForm
from Article.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comments_text']
