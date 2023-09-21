from django.shortcuts import render
from .models import Aricle

# Create your views here.
def throw(request):
    return render(request,'app/throw.html')

def catch(request):
    name = request.GET.get('name')
    context = {
        'name':name
    }
    return render(request,'app/catch.html',context)

def new(request):
    return render(request,'app/new.html')

def store(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Aricle()
    article.title = title
    article.content = content
    article.save()
    print(title,content)
    return render(request,'app/store.html')