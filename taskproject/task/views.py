from datetime import timedelta

from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from django.shortcuts import render, redirect
from .models import Task, Tag, Subscription
from .forms import TaskForm
from .tasks import generate_task_report_task

from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def task_list(request):
    tasks = Task.objects.all()
    filters = ('status', 'priority', 'tags')
    search_query = request.GET.get('search')

    for f in filters:
        value = request.GET.get(f)
        if value:
            tasks = tasks.filter(**{f'{f}__name' if f == 'tag' else f: value})
    if search_query:
        tasks = tasks.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))

    tasks = tasks.order_by('-priority', 'created_at')
    all_tags = Tag.objects.all()

    paginator = Paginator(tasks, 10)
    page = request.GET.get('page')
    tasks = paginator.get_page(page)

    return render(request, 'tasks/task_list.html', {
        'Task': Task,
        'tasks': tasks,
        'status_filter': request.GET.get('status'),
        'priority_filter': request.GET.get('priority'),
        'all_tags': all_tags,
        'tag_filter': request.GET.get('tag'),
    })


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            subscription = Subscription.objects.create(user=request.user, task=task)
            print(f"Created subscription: {subscription}")
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


def task_update(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

            return redirect('task_list')

    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})




def task_delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('task_list')




def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')  # Замените на URL вашей страницы после регистрации
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


