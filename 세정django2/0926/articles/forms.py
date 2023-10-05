from django import forms
from .models import Article

# 사용자에게 입력받기 위한 양식을 만들어주는 class작성
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField()

# form에 포함되어야 할 요소를 위처럼 직접선언한는것이 아니라 Model에서 참조  ->> ModelForm
# Model + Form 의 역할을 하는 클래스
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']
        
    