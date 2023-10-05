from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.
def index(request):
    #게시글 목록 조회해서 템플릿에 전달
    #1. 게시글 목록 DB에서 조회
    #    ORM 이용해야 하는데 >> 이 역할을 Model class(Article)가 수행
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }

    return render(request,'articles/index.html',context)

def new(request):
    form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request,'articles/new.html',context)

def create(request):
    # 요청에서 데이터 받아와서 DB에 저장하고
    title = request.POST.get('title')
    content = request.POST.get('content')
    # ModelForm으로 만들어진 form에서 사용자가 데이터를 입력
    # 어떤 데이터가 들어올지 알수 있음
    # 요청에서 데이터를 따로 받아오는게 아니라 ..한꺼번에 받아올 수 있다
    # Article.objects.create()
    article = Article(title=title,content=content)
    article.save()
    
    return redirect('articles:index')

def delete(request,pk):

    # DB에서 삭제하고 목록조회해서 템플릿에 전달
    # record 단위는 instance로 처리...
    article = Article.objects.get(pk=pk)
    article.delete()
    # articles = Article.objects.all()
    # context = {
    #     'articles' :articles
    # }
    # return render(request,'articles/index.html', context)
    return redirect('articles:index')

# 상세 페이지 보여달라는 요청을 처리하는 함수
def detail(request,pk):
    #DB에서 pk에 해당하는 게시글 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request,'articles/detail.html',context)

# 수정 화면 보여달라는 요청 처리하는 함수
def edit(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request,'articles/update.html',context)

# 사용자가 입력한 내용을 DB에 저장하기
def update(request,pk):
    #원래 db에 저장되어있던 내용 불러오기
    article = Article.objects.get(pk=pk)
    #내용수정
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:index')



