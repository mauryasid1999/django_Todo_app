from django.shortcuts import render,redirect
from .models import ToDoList,Category

def index(request):
    todos=ToDoList.objects.all()
    categories=Category.objects.all()

    if request.method=="POST":
         if "taskAdd" in request.POST:
             title=request.POST["description"]
             date = str(request.POST["date"])
             category = request.POST["category_select"] 
             content = title + " -- " + date + " " + category
             Todo=ToDoList(title=title, content=content, due_date=date)
             Todo.save()
             return redirect('/')
    
    return render(request, "index.html", {"todos": todos, "categories":categories})