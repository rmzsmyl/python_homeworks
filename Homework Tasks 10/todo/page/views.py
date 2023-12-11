from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from . models import Todo

def index(request):
    return render(request, 'index.html')

def add(request):
    obj = Todo()

    obj.title = request.POST['title']
    obj.desc = request.POST['description']
    obj.priority = request.POST['priority']
    obj.created_at = request.POST['time']
    
    obj.save()
    return render(request, 'list.html')

def edit(request, id):
    obj = Todo.objects.get(id=id)
    title = obj.title
    description = obj.desc
    priority = obj.priority
    time = obj.created_at
    id = obj.id

    context = {
        'title': title,
        'description': description,
        'priority': priority,
        'time': time,
        'id': id
    }

    return render(request, 'edit.html', context)

def update(request, id):
    alltodos = Todo.objects.all()
    obj = Todo(id=id)
    obj.title = request.POST['title']
    obj.desc = request.POST['description']
    obj.priority = request.POST['priority']
    obj.created_at = request.POST['time']
    obj.save()

    context = {
        'alltodos': alltodos
    }

    return render(request, 'list.html', context)



def delete(request, id):
   alltodos = Todo.objects.all()
   obj = Todo.objects.get(id = id)
   obj.delete()

   return redirect('list')




# def list(request):
#     alltodos = Todo.objects.all()
#     return render(request, 'list.html', {'alltodos': alltodos})


class TodoList(ListView):
    model = Todo
    template_name = 'list.html'
    context_object_name = 'alltodos'

def search (request):
    srch = request.POST ['query']
    alltodos = Todo.objects.filter(title__contains= srch)
    context = {
        'alltodos': alltodos
    }
    
    return render(request, 'list.html', context)

