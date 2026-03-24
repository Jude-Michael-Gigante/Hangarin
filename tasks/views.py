from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category, Priority

# Dashboard
def dashboard(request):
    tasks = Task.objects.all()
    return render(request, 'dashboard.html', {'tasks': tasks})

# Category CRUD
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_add(request):
    if request.method == 'POST':
        name = request.POST['name']
        Category.objects.create(name=name)
        return redirect('category_list')
    return render(request, 'category_form.html')

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.save()
        return redirect('category_list')
    return render(request, 'category_form.html', {'category': category})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')

# Priority CRUD
def priority_list(request):
    priorities = Priority.objects.all()
    return render(request, 'priority_list.html', {'priorities': priorities})

def priority_add(request):
    if request.method == 'POST':
        name = request.POST['name']
        Priority.objects.create(name=name)
        return redirect('priority_list')
    return render(request, 'priority_form.html')

def priority_edit(request, pk):
    priority = get_object_or_404(Priority, pk=pk)
    if request.method == 'POST':
        priority.name = request.POST['name']
        priority.save()
        return redirect('priority_list')
    return render(request, 'priority_form.html', {'priority': priority})

def priority_delete(request, pk):
    priority = get_object_or_404(Priority, pk=pk)
    priority.delete()
    return redirect('priority_list')

# Task CRUD
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_add(request):
    if request.method == 'POST':
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            deadline=request.POST['deadline'],
            status=request.POST['status'],
            category=get_object_or_404(Category, pk=request.POST['category']),
            priority=get_object_or_404(Priority, pk=request.POST['priority']),
        )
        return redirect('task_list')
    categories = Category.objects.all()
    priorities = Priority.objects.all()
    return render(request, 'task_form.html', {'categories': categories, 'priorities': priorities})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.deadline = request.POST['deadline']
        task.status = request.POST['status']
        task.category = get_object_or_404(Category, pk=request.POST['category'])
        task.priority = get_object_or_404(Priority, pk=request.POST['priority'])
        task.save()
        return redirect('task_list')
    categories = Category.objects.all()
    priorities = Priority.objects.all()
    return render(request, 'task_form.html', {'task': task, 'categories': categories, 'priorities': priorities})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')