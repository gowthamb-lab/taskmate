from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def todolist(request):
    #print("I am here in the todolist view")
    #return HttpResponse("This is the To-Do Lis app view")

    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).manage = request.user
            form.save()
            #all_tasks= TaskList.objects.all
            #context = {'welcome_text': 'Welcome from Jnja2 template'}
            messages.success(request, ('New Task Added!'))
        return redirect('todolist')
    else:

        all_tasks= TaskList.objects.all().filter(manage=request.user)
        paginator = Paginator(all_tasks, 10)
        page_number = request.GET.get('page')
        all_tasks = paginator.get_page(page_number) 
        #context = {'welcome_text': 'Welcome from Jnja2 template'}
        return render(request, 'todolist.html', {'all_tasks': all_tasks})


def index(request):
    context = {'index_text': 'Welcome from Jnja2 template to index page'}
    return render(request, 'index.html', context)

def about(request):
    context = {'about_text': 'Welcome from Jnja2 template to about page'}
    return render(request, 'about.html', context)

def contact(request):
    context = {'contact_text': 'Welcome from Jnja2 template to contact page'}
    return render(request, 'contact.html', context)    

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage != request.user:
        messages.error(request, ('Access Restricted, You are not allowed!'))
        return redirect('todolist')
    task.delete()
    messages.success(request, ('Task Deleted!'))
    return redirect('todolist')

@login_required
def edit_task(request, task_id):
    if request.method == 'POST':
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, ('Task Edited!'))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})

@login_required    
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage != request.user:
        messages.error(request, ('Access Restricted, You are not allowed!'))
        return redirect('todolist') 
    task.done = True
    task.save()
    messages.success(request, ('Task Marked as Completed!'))
    return redirect('todolist') 

@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage != request.user:
        messages.error(request, ('Access Restricted, You are not allowed!'))
        return redirect('todolist')
    task.done = False
    task.save()
    messages.success(request, ('Task Marked as Pending!'))
    return redirect('todolist')
