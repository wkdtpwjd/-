from django.shortcuts import render,redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request,'movies/index.html',context)

def detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie':movie,
    }
    return render(request,'movies/detail.html',context)

# def create(request):  # 작성폼도 보여주고 
#     form = MovieForm()
#     context = {
#         'form':form,
#     }
#     return render(request,'movies/create.html',context)

def create2(request):  # 작성데이터 저장
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # movie = Movie(title=title,content=content)
    # movie.save()
    # return redirect('movies:index')
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail',movie.pk)
    else:
        form = MovieForm()
    context = {
        'form':form,
    }
    return render(request,'movies/create2.html',context)






def delete(request,pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')


# def update(request,pk):
#     movie = Movie.objects.get(pk=pk)
#     form = MovieForm(instance=movie)
#     context = {
#         'movie':movie,
#         'form': form,
#     }
#     return render(request,'movies/update.html',context)


def update2(request,pk):
    movie = Movie.objects.get(pk=pk)
    if request.method =='POST':
        form = MovieForm(request.POST,instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail',movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form':form,
        'movie':movie,
    }
    return render(request,'movies/update2.html',context)  