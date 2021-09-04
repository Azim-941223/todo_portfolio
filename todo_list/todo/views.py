from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm, TodoForm, UserAuthenticationForm
from .models import *


@login_required
def index(request):
    """Home page"""
    if request.method == 'POST':
        """Creating a task"""
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            messages.success(request, f'Таск {todo.title}, успешно добавлен!')
            return redirect('home')
    form = TodoForm()
    todos = Todo.objects.filter(author=request.user)
    return render(request, 'todo/index.html', {'todos': todos, 'form': form})


@login_required
def update_task(request, pk):
    """Updating a task"""
    todo = Todo.objects.get(pk=pk, author=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Тodo успешно обновлен!')
            return redirect('home')
    form = TodoForm(instance=todo)
    return render(request, 'todo/update.html', {'form': form})


@login_required
def complete(request, pk):
    """Update task to complete"""
    todo = Todo.objects.get(pk=pk)
    todo.complete = True
    todo.save()
    messages.success(request, f'Таск {todo.title}, выполнен!')
    return redirect('home')


@login_required
def un_complete(request, pk):
    """Update task to not complete"""
    todo = Todo.objects.get(pk=pk)
    todo.complete = False
    todo.save()
    messages.success(request, f'Таск {todo.title}, больше не выполнен!')
    return redirect('home')


@login_required
def delete(request, pk):
    """Deleting a task"""
    Todo.objects.get(pk=pk).delete()
    messages.success(request, 'Таск упешно удален!')
    return redirect('home')


def sign_up(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'project/form.html', {'form': form, 'btn_text': 'Зарегистрироваться'})


def sign_in(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
    else:
        form = UserAuthenticationForm()
    return render(request, 'project/form.html', {'form': form, 'btn_text': 'Войти'})


def sign_out(request):
    logout(request)
    return redirect('home')