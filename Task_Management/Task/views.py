from django.shortcuts import render, redirect
from .forms import TaskStoreForm
from .models import TaskStoreModel

def store_task(request):
    if request.method == 'POST':
        form = TaskStoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    else:
        form = TaskStoreForm()
    return render(request, 'store_task.html', {'form': form})

def show_task(request):
    tasks = TaskStoreModel.objects.filter(Status=False)
    return render(request, 'show_task.html', {'tasks': tasks})

def edit_task(request, Title):
    task = TaskStoreModel.objects.get(Title=Title)
    if request.method == 'POST':
        form = TaskStoreForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    else:
        form = TaskStoreForm(instance=task)
    return render(request, 'store_task.html', {'form': form})


def completed_tasks(request):
    completed_tasks = TaskStoreModel.objects.filter(Status = True)
    return render(request, 'completed_tasks.html', {'completed_tasks': completed_tasks})


def delete_task(request, Title):
    TaskStoreModel.objects.filter(Title = Title).delete()
    return redirect('show_task')

def complete_task(request, Title):
    task = TaskStoreModel.objects.get(Title = Title)
    task.Status = True
    task.save()
    return redirect('completed_tasks')


