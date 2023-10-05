from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     #제목
#     #내용 
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)  # form class 에서 max-length 는 필수인자가 아니다
    
class ArticleForm(forms.ModelForm):  # 앞에는 파일명
    title = forms.CharField(
        label ='제목',
        widget=forms.TextInput(
            attrs={
                'class':'my-title'
            }
        )
    )
    # model 등록만 하면 끝
    class Meta:
        model = Article
        fields = '__all__'
    