# from .models import Article, Comment


# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ('title','content',)


from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title','description',)