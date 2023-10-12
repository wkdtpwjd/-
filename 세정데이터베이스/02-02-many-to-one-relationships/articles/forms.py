from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','content',)
        #exclude = ('user',) 위랑 같은 표현

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
