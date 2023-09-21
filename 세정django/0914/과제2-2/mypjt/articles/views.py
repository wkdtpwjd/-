from django.shortcuts import render
from .models import Article

# Create your views here.
def throw(request):
    return render(request,"articles/throw.html")


def catch(request):   # 사용자가 던진 데이터 받아오기, 어디서 받아요 ? 요청객체 에서 꺼내오기
    name = request.GET.get('name')
    context = {
        'name' : name,
    }
    return render(request,"articles/catch.html",context)


def new(request):
    # 사용자가 입력할 수 있는 화면 제공
    return render(request,"articles/new.html")

def create(request):
    # 사용자가 입력한 데이터 받아서 DB에 저장하고 
    # 저장되었습니다
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 모델을 이용해서 DB에 저장하기
    article = Article()
    article.title = title
    article.content = content
    #DB에 저장
    article.save()
    
    return render(request,'articles/create.html')