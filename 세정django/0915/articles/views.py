from django.shortcuts import render,redirect
from .models import Article

# Create your views here.
def index(request):
    # 게시글 목록 조회해서 템플릿에 전달
    # 게시글목록 DB에서 조회
    # ORM 이용해야 하는데 >> 이역할을 Model class(Article)
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request,'articles/index.html',context)

def new(request):

    return render(request,'articles/new.html')

def create(request):
    # 요청에서 데이터 받아와서 DB에 저장하고
    title = request.POST.get('title')
    content = request.POST.get('content')
    # Article.objects.create()
    article = Article(title=title,content=content)
    article.save()
    articles = Article.objects.all()
    # context = {
    #     'articles':articles
    # }
    # 목록 조회해서 템플릿에 전달
    # index한테 다시 요청해라라는 응답 redirect
    return redirect(request.u)

def delete(request,num):
        # DB에서 삭제하고 목록조회해서 템플릿에 전달
    instance = Article.objects.get(pk=p2):
    article.e
    )
    return render(request,'articles/index.html')
