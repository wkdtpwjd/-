from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request,'libraries/index.html',context)


# def create(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             article = form.save(commit=False)  # 기본값은 True , 데이터 베이스에 요청을 보내지는 않고 메서드기때문에 return값은 주겠다.
#             article.user = request.user
#             # article.save() 같은결과다
#             form.save() 
#             return redirect('articles:detail', article.pk)
#     else:
#         form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/create.html', context)
def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libraries:index')
    else:
        form = BookForm()
    context = {
        'form':form,
    }
    return render(request,'libraries/create.html',context)


def detail(request,pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book':book,
    }
    return render(request,'libraries/detail.html',context)


def delete(request,pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('libraries:index')


def update(request,pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('libraries:detail',book.pk)
    else:
        form =BookForm(instance=book)
    context = {
        'book':book,
        'form':form,
    }
    return render(request,'libraries/update.html',context)