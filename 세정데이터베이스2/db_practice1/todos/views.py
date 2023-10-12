from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_http_methods,require_POST
from .models import Todo
from .forms import TodoForm
# Create your views here.
@login_required
@require_safe
def index(request):
    todos = request.user.todo_set.all()
    todo_form = TodoForm()
    context = {
        'todos' : todos,
        'todo_form' : todo_form,
    }
    return render(request,'todos/index.html',context)

@login_required
@require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'POST':
        form = TodoForm(data=request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            form.save()
            return redirect('todos:index')
@login_required
@require_http_methods(['POST'])
def update(request,pk):
    todo = Todo.objects.get(pk=pk)
    form = TodoForm(data=request.POST,instance=todo)
    print(request.POST)
    if form.is_valid():
        form.save()
    return redirect('todos:index')
@login_required
def delete(request,pk):
    if request.method=='POST':
        todo = Todo.objects.get(pk=pk)
        todo.delete()
    return redirect('todos:index')
