from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    if request.method == 'POST':
        add_todo = TodoForm(request.POST)
        if add_todo.is_valid:
            add_todo.save()
            return redirect("/")

    context = {
        'todos': Todo.objects.all(),
        'form': TodoForm()
    }
    return render(request, 'home.html', context)


def delete(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('/')
    return render(request, 'delete.html', {'todo': todo})


def clear_all(request):
    todos = Todo.objects.all()
    todos.delete()
    return redirect("/")


def update_todo(request, id):
    befor_update = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo = TodoForm(request.POST, instance=befor_update)
        if todo.is_valid:
            todo.save()
            return redirect("/")
    else:
        todo = TodoForm(instance=befor_update)

    return render(request, 'update.html', {'todo': todo})
