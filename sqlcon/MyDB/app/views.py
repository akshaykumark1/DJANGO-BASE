from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        new_todo = Todo(title=title)
        new_todo.save()
    return redirect('todo_list')

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo_list')

def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.complete = not todo.complete
    todo.save()
    return redirect('todo_list')

