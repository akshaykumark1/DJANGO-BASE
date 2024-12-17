from django.shortcuts import render, redirect
from .models import TodoItem

# Create your views here.
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('todo')
        todo_obj = TodoItem(title1=title)
        todo_obj.save()
        return redirect("add_todo")
    todo_obj = TodoItem.objects.all()
    return render(request, "index.html", {'todos': todo_obj})

def delete_g(request, pk):
    todo_obj = TodoItem.objects.get(pk=pk)
    todo_obj.delete()
    return redirect("add_todo")

def edit_g(request, pk):
    if request.method == 'POST':
        title1 = request.POST.get('todo')
        TodoItem.objects.filter(pk=pk).update(title1=title1)
        return redirect('add_todo')
    todo_obj = TodoItem.objects.get(pk=pk)
    return render(request, 'index.html', {'editor': todo_obj})
