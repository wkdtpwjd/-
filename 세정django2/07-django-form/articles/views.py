from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form':form,
#     }
#     return render(request, 'articles/new.html',context)


def create(request):
    # if 요청의 메서드가 post라면 :
    # create 로직 구현
    #else 요청의 메서드가 post가 아니라면
    # new 로직
    if request.method == 'POST':
        form = ArticleForm(request.POST)
    # 유효성 검사   
    # 유효성 검사가 통과된 경우
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail',article.pk)
    # 통과하지 못하면 실패한 이유가 담긴 form이 나온다 = 에러메시지가 나옴


    else:
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request, 'articles/create.html',context)








    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title=title, content=content)
    # article.save()
    # return redirect('articles:index')


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form':form,
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 요청메서드가 POST라면 (update)
    # 요청메서드가 GET라면 (edit)
    if request.method == 'POST':
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid:
            form.save()   # 생성이냐 수정이냐를 판단해야함 위의 instance가 있으면 수정이구나...
            return redirect('articles:detail',article.pk)

    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form':form,
    }
    return render(request, 'articles/edit.html', context)

 



    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # return redirect('articles:detail', article.pk)
