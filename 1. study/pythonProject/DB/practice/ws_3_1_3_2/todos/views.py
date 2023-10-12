from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    # todos = Todo.objects.all()
    # 아래 방식 기억하기(내꺼만 볼꺼야!)
    todos = request.user.todo_set.all()
    context = {
        'todos' : todos,
    }
    return render(request, 'todos/index.html', context)


def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False) # todo(객체)만 리턴
            todo.author = request.user
            form.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form' : form
    } 
    return render(request, 'todos/create.html', context)

def toggle(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    todo = Todo.objects.get(pk=pk)
    if todo.author == request.user:
        todo.completed = not todo.completed
        todo.save()
    
    return redirect('todos:index')


def delete(request, todo_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    todo = Todo.objects.get(pk=todo_pk)
    if todo.author == request.user:
        todo.delete()
    return redirect('todos:index')