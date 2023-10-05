from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    # 데이터베이스의 전체 게시글을 조회하고 
    # 출력해야하는 역할
    # 모델.objects.all()
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request,'articles/index.html',context)

def detail(request,pk): #여기서는 전체조회가 아니라 단일게시글조회
    article = Article.objects.get(pk=pk)  # 왼쪽pk => table의 컬럼이름이고 , 오른쪽 pk => 변수이름
    context = {
        'article':article,
    }
    return render(request,'articles/detail.html',context)

def new(request):
    return render(request,'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content= request.GET.get('content')

    # 저장하는 방법 3가지
    #1 
    # 단점 코드길다
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2 
    article = Article(title=title,content=content)
    article.save()

    # 3  
    # 단점 유효성검사를 못함
    # Article.objects.create(title=title, content=content)
    return render(request,'articles/create.html')